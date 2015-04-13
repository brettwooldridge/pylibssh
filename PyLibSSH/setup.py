from setuptools import setup, find_packages

setup(
   name = "pylibssh",
   version = "0.1",
   packages = find_packages(),

   # metadata for upload to PyPI
   author = "Brett Wooldridge",
   author_email = "brett.wooldridge@gmail.com",
   description = "This package provides CFFI bindings to libssh",
   license = "Apache License 2.0",
   keywords = "libssh ssh ssh1 ssh2",
   url = "https://github.com/brettwooldridge/pylibssh",
)
