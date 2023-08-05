from sklearn.base import BaseEstimator
from sklearn.exceptions import NotFittedError
try:
	from sklearn.compose import ColumnTransformer
except ImportError:
	class ColumnTransformer:
		pass
try:
	from sklearn.feature_selection._base import SelectorMixin
except ImportError:
	from sklearn.feature_selection.base import SelectorMixin
from sklearn.feature_selection import SelectFromModel
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn_pandas import DataFrameMapper
from sklearn2pmml.resources import _package_classpath
from subprocess import PIPE, Popen
from zipfile import ZipFile

import joblib
import numpy
import os
import pandas
import platform
import re
import sklearn
import sklearn_pandas
import tempfile

from .metadata import __copyright__, __license__, __version__
from .pipeline import PMMLPipeline

def _is_categorical(dtype):
	if dtype == object or dtype == str or dtype == bool:
		return True
	elif _is_pandas_categorical(dtype):
		return True
	return False

def _is_pandas_categorical(dtype):
	if hasattr(dtype, "name"):
		return dtype.name == "category"
	return False

class EstimatorProxy(BaseEstimator):

	def __init__(self, estimator, attr_names = ["feature_importances_"]):
		self.estimator = estimator
		self.attr_names = attr_names
		try:
			self._copy_attrs()
		except NotFittedError:
			pass

	def _copy_attrs(self):
		for attr_name in self.attr_names:
			if hasattr(self.estimator, attr_name):
				setattr(self, attr_name, getattr(self.estimator, attr_name))

	def fit(self, X, y = None, **fit_params):
		self.estimator.fit(X, y, **fit_params)
		self._copy_attrs()
		return self

	def predict(self, X, **predict_params):
		return self.estimator.predict(X, **predict_params)

	def predict_proba(self, X, **predict_proba_params):
		return self.estimator.predict_proba(X, **predict_proba_params)

class SelectorProxy(BaseEstimator):

	def __init__(self, selector):
		self.selector = selector
		try:
			self._copy_attrs()
		except NotFittedError:
			pass

	def _copy_attrs(self):
		try:
			setattr(self, "support_mask_", self.selector._get_support_mask())
		except ValueError:
			pass

	def fit(self, X, y = None, **fit_params):
		self.selector.fit(X, y, **fit_params)
		self._copy_attrs()
		return self

	def transform(self, X):
		return self.selector.transform(X)

def _get_steps(obj):
	if isinstance(obj, Pipeline):
		return obj.steps
	elif isinstance(obj, BaseEstimator):
		return [("estimator", obj)]
	else:
		raise TypeError("The object is not an instance of {0}".format(BaseEstimator.__name__))

def _escape(obj, escape_func):
	if isinstance(obj, DataFrameMapper):
		obj.features = _escape_steps(obj.features, escape_func = escape_func)
		if hasattr(obj, "built_features"):
			if obj.built_features is not None:
				obj.built_features = _escape_steps(obj.built_features, escape_func = escape_func)
	elif isinstance(obj, ColumnTransformer):
		obj.transformers = _escape_steps(obj.transformers, escape_func = escape_func)
		obj.remainder = escape_func(obj.remainder, escape_func = escape_func)
		if hasattr(obj, "transformers_"):
			obj.transformers_ = _escape_steps(obj.transformers_, escape_func = escape_func)
	elif isinstance(obj, FeatureUnion):
		obj.transformer_list = _escape_steps(obj.transformer_list, escape_func = escape_func)
	elif isinstance(obj, Pipeline):
		obj.steps = _escape_steps(obj.steps, escape_func = escape_func)
	elif isinstance(obj, SelectorMixin):
		return SelectorProxy(obj)
	elif isinstance(obj, list):
		return [escape_func(e, escape_func = escape_func) for e in obj]
	return obj

def _escape_steps(steps, escape_func):
	return [(step[:1] + (escape_func(step[1], escape_func = escape_func), ) + step[2:]) for step in steps]

def make_pmml_pipeline(obj, active_fields = None, target_fields = None, escape_func = _escape):
	"""Translates a regular Scikit-Learn estimator or pipeline to a PMML pipeline.

	Parameters:
	----------
	obj: BaseEstimator
		The object.

	active_fields: list of strings, optional
		Feature names. If missing, "x1", "x2", .., "xn" are assumed.

	target_fields: list of strings, optional
		Label name(s). If missing, "y" is assumed.

	"""
	steps = _escape_steps(_get_steps(obj), escape_func = escape_func)
	pipeline = PMMLPipeline(steps)
	if active_fields is not None:
		pipeline.active_fields = numpy.asarray(active_fields)
	if target_fields is not None:
		pipeline.target_fields = numpy.asarray(target_fields)
	return pipeline

def _make_java_command(java_home, java_opts, java_args):
	result = []
	if java_home is not None:
		if not isinstance(java_home, str):
			raise ValueError()
		result.extend([os.path.join(java_home, "bin", "java")])
	else:
		result.extend(["java"])
	if java_opts is not None:
		if not isinstance(java_opts, list):
			raise ValueError()
		result.extend(java_opts)
	if not isinstance(java_args, list):
		raise ValueError()
	result.extend(java_args)
	return result

def _java_version(java_home = None):
	cmd = _make_java_command(java_home = java_home, java_opts = None, java_args = ["-version"])
	try:
		process = Popen(cmd, stdout = PIPE, stderr = PIPE, bufsize = 1, universal_newlines = True)
	except:
		return None
	output, error = process.communicate()
	retcode = process.poll()
	if retcode:
		return None
	return _parse_java_version(error)

def _parse_java_version(java_version):
	match = re.match("^(.*)\sversion\s\"(.*)\"(|\s.+)$", java_version, re.MULTILINE)
	if match:
		return (match.group(1), match.group(2))
	else:
		return None

def _classpath(user_classpath):
	return _package_classpath() + user_classpath

def _process_classpath(name, fun, user_classpath):
	jars = _classpath(user_classpath)
	for jar in jars:
		with ZipFile(jar, "r") as zipfile:
			try:
				zipentry = zipfile.getinfo(name)
			except KeyError:
				pass
			else:
				fun(zipfile.open(zipentry))

def _dump(obj, prefix):
	fd, path = tempfile.mkstemp(prefix = (prefix + "-"), suffix = ".pkl.z")
	try:
		joblib.dump(obj, path, compress = 3)
	finally:
		os.close(fd)
	return path

def sklearn2pmml(pipeline, pmml, with_repr = False, java_home = None, java_opts = None, user_classpath = [], debug = False):
	"""Converts a fitted PMML pipeline object to PMML file.

	Parameters:
	----------
	pipeline: PMMLPipeline
		The input PMML pipeline object.

	pmml: string
		The path to output PMML file.

	with_repr: boolean, optional
		If true, insert the string representation of pipeline into the PMML document.

	java_home: string, optional
		The path to Java installation directory.
		Functionally analogous to the JAVA_HOME environment variable.

	java_opts: list of strings, optional
		Java options.
		Functionally analogous to the JAVA_OPTS environment variable.

	user_classpath: list of strings, optional
		The paths to JAR files that provide custom Transformer, Selector and/or Estimator converter classes.
		The SkLearn2PMML classpath is constructed by appending user JAR files to package JAR files.

	debug: boolean, optional
		If true, print information about the conversion process.

	"""
	if debug:
		java_version = _java_version(java_home = java_home)
		if java_version is None:
			java_version = ("java", "N/A")
		print("python: {0}".format(platform.python_version()))
		print("sklearn: {0}".format(sklearn.__version__))
		print("sklearn2pmml: {0}".format(__version__))
		print("joblib: {0}".format(joblib.__version__))
		print("sklearn_pandas: {0}".format(sklearn_pandas.__version__))
		print("pandas: {0}".format(pandas.__version__))
		print("numpy: {0}".format(numpy.__version__))
		print("{0}: {1}".format(java_version[0], java_version[1]))
	if not isinstance(pipeline, PMMLPipeline):
		raise TypeError("The pipeline object is not an instance of {0}. Use the 'sklearn2pmml.make_pmml_pipeline(obj)' utility function to translate a regular Scikit-Learn pipeline or estimator to a PMML pipeline".format(PMMLPipeline.__name__))
	if with_repr:
		pipeline.repr_ = repr(pipeline)
	dumps = []
	try:
		java_args = ["-cp", os.pathsep.join(_classpath(user_classpath)), "com.sklearn2pmml.Main"]
		estimator = pipeline._final_estimator
		# if isinstance(estimator, H2OEstimator):
		if hasattr(estimator, "download_mojo"):
			# Avoid MOJO (re-)download if the indicator attribute is set
			if not hasattr(estimator, "_mojo_path"):
				estimator_mojo = estimator.download_mojo()
				dumps.append(estimator_mojo)
				estimator._mojo_path = estimator_mojo
		pipeline_pkl = _dump(pipeline, "pipeline")
		java_args.extend(["--pkl-pipeline-input", pipeline_pkl])
		dumps.append(pipeline_pkl)
		java_args.extend(["--pmml-output", pmml])
		cmd = _make_java_command(java_home = java_home, java_opts = java_opts, java_args = java_args)
		if debug:
			print("Executing command:\n{0}".format(" ".join(cmd)))
		try:
			process = Popen(cmd, stdout = PIPE, stderr = PIPE, bufsize = 1, universal_newlines = True)
		except OSError:
			raise RuntimeError("Java is not installed, or the Java executable is not on system path")
		output, error = process.communicate()
		retcode = process.poll()
		if debug or retcode:
			if len(output) > 0:
				print("Standard output:\n{0}".format(output))
			else:
				print("Standard output is empty")
			if len(error) > 0:
				print("Standard error:\n{0}".format(error))
			else:
				print("Standard error is empty")
		if retcode:
			raise RuntimeError("The SkLearn2PMML application has failed. The Java executable should have printed more information about the failure into its standard output and/or standard error streams")
	finally:
		if debug:
			print("Preserved joblib dump file(s): {0}".format(" ".join(dumps)))
		else:
			for dump in dumps:
				os.remove(dump)

def _parse_properties(lines):
	splitter = re.compile("\s*=\s*")
	properties = dict()
	for line in lines:
		line = line.decode("UTF-8").rstrip()
		if line.startswith("#"):
			continue
		key, value = splitter.split(line)
		properties[key] = value
	return properties

def _format_properties(properties):
	return ["{0} = {1}\n".format(k, v) for k, v in properties.items()]

def _expand_complex_key(key):
	begin = key.find("(")
	end = key.find(")", begin + 1)
	if begin < 0 or end < 0:
		return [key]

	prefix = key[:begin]
	body = key[begin + 1:end]
	suffix = key[end + 1:]

	result = []
	parts = body.split("|")
	for part in parts:
		result += _expand_complex_key(prefix + part + suffix)
	return result

def _expand_mapping(mapping):
	result = dict()
	for k, v in mapping.items():
		pythonClazzes = _expand_complex_key(k)
		javaClazz = v
		for pythonClazz in pythonClazzes:
			result[pythonClazz] = (javaClazz if javaClazz else pythonClazz)
	return result

def load_class_mapping(user_classpath = []):
	"""Loads the class mapping.

	Parameters:
	----------
	user_classpath: list of strings, optional
		The paths to JAR files that provide custom Transformer, Selector and/or Estimator converter classes.

	Returns:
	-------
	mapping: dict
		Mapping from Python class names to Java converter class names.

	"""
	mapping = dict()
	processor = lambda x: mapping.update(_expand_mapping(_parse_properties(x.readlines())))
	_process_classpath("META-INF/sklearn2pmml.properties", processor, user_classpath)
	return mapping

def make_class_mapping_jar(path, mapping):
	"""Generates a class mapping JAR file.

	Parameters:
	----------
	path: string
		The path to output JAR file.

	mapping: dict of strings
		Mapping from Python class names to Java converter class names.

	"""
	lines = _format_properties(mapping)

	with ZipFile(path, mode = "w") as zipfile:
		zipfile.writestr("META-INF/sklearn2pmml.properties", "".join(lines))

def _strip_module(name):
	parts = name.split(".")
	if len(parts) > 1:
		parts.pop(-2)
		return ".".join(parts)
	return name
