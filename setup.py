import pybind11
from distutils.core import setup, Extension

module1 = Extension('example',
                    sources=['example.cpp'],
                    include_dirs=[pybind11.get_include(False),
                                  pybind11.get_include(False)],
                    extra_compile_args=['-O3', '-Wall', '-shared', '-std=c++11',
                                        '-fPIC'],
                    language='c++')

setup(name='example',
      ext_modules=[module1],
      install_requires=['pybind11', ],)
