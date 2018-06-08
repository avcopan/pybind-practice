import pybind11
from distutils.core import setup, Extension

module1 = Extension('example',
                    sources=['example.cpp'],
                    include_dirs=[pybind11.get_include(False),
                                  pybind11.get_include(False)],
                    language='c++')

setup(name='example',
      ext_modules=[module1])
