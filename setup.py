import sys
from distutils.core import setup, Extension
from pybind11 import get_include as get_pybind_inc
from distutils.sysconfig import get_python_inc


# Lists of flags for the compiler
include_dirs = [get_python_inc(), get_pybind_inc()]
compile_args = ['-O3', '-Wall', '-shared', '-std=c++11', '-fPIC']
link_args = []

# Optionally, for testing purposes, pass the '--coverage' flag to gcc
if '--cc' in sys.argv:
    compile_args.append('--coverage')
    link_args.append('--coverage')
    sys.argv.remove('--cc')

# This defines how the C++ shared object will be compiled
module = Extension('pybind_example',
                   sources=['pybind_example.cpp'],
                   include_dirs=include_dirs,
                   extra_compile_args=compile_args,
                   extra_link_args=link_args,
                   language='c++')

# This function performs the installation
setup(name='pybind_example',
      ext_modules=[module],
      install_requires=['pybind11', ],)
