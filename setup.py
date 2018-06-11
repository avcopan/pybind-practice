import sys
import pybind11
from distutils.core import setup, Extension
from distutils.sysconfig import get_python_inc


# Lists of flags for the compiler
include_dirs = [get_python_inc(),
                pybind11.get_include(False),
                pybind11.get_include(True)]
compile_args = ['-O3', '-Wall', '-shared', '-std=c++11', '-fPIC']
link_args = []

if '--codecov' in sys.argv:
    compile_args.append('--coverage')
    link_args.append('--coverage')
    sys.argv.remove('--codecov')

module = Extension('pybind_example',
                   sources=['pybind_example.cpp'],
                   include_dirs=include_dirs,
                   extra_compile_args=compile_args,
                   extra_link_args=link_args,
                   language='c++')

setup(name='pybind_example',
      ext_modules=[module],
      install_requires=['pybind11', ],)
