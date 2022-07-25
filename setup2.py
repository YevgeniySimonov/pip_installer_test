import os
import sys
import subprocess

from Cython.Build import cythonize
from setuptools import find_packages
from setuptools.command.build_ext import build_ext

try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension

# compile: python3 setup.py build_ext --inplace

path = os.path.dirname(os.path.realpath(__file__))
defs = [('NPY_NO_DEPRECATED_API', 0)]

print('compillation path: ', path)

class BuildExt(build_ext):
    """Customized setuptools build_ext command - builds protos on build."""
    def run(self):
        protoc_command = ["make", "cython-build"]
        if subprocess.call(protoc_command) != 0:
            sys.exit(-1)
        build_ext.run(self)
    
setup(
    author="Yevgeniy Simonov",
    description="""Test pip installer""",
    name="Test pip installer",
    packages=find_packages(exclude=('tests', 'examples', 'docs')),
    ext_modules=cythonize(
        [
            Extension(
                "pip_installer_test.pip_installer_test",
                sources=[
                    os.path.normpath(os.path.join(path, 'pip_installer_test', 'dummy_program.pyx')),
                    os.path.normpath(os.path.join(path, 'pip_installer_test', 'src', 'dummyProgram.cpp'))
                ],
                language='c++',
                extra_compile_args=["-w", "-std=c++11"],
                include_dirs=["pip_installer_test"],
                define_macros=defs        
            )
        ], 
        language_level = "3",
        annotate=False,  # this flag if set to true generates html annotation
        nthreads=4
    ),
    setup_requires=[
        'setuptools >= 18.0',
        'cython'
    ],
    zip_safe=True,
    has_ext_modules=lambda: True,
    include_dirs=['pip_installer_test/'],
    # cmdclass={'build_ext': BuildExt}
)   