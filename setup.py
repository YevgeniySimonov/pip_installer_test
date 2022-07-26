import os
import sys
import subprocess

from Cython.Build import cythonize
from setuptools import find_packages
from setuptools.command.build_ext import build_ext
from setuptools.command.install import install
from setuptools.command.build_py import build_py

try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension

# compile: python3 setup.py build_ext --inplace

path = os.path.dirname(os.path.realpath(__file__))

print('compillation path: ', path)

class BuildExt(build_ext):
    """Customized setuptools build_ext command - builds protos on build."""
    def run(self):
        protoc_command = ["make", "cython-build"]
        if subprocess.call(protoc_command) != 0:
            sys.exit(-1)
        build_ext.run(self)
    
class Install(install):
    """Customized setuptools build_ext command - builds protos on build."""
    def run(self):
        protoc_command = ["make", "cython-build"]
        if subprocess.call(protoc_command) != 0:
            sys.exit(-1)
        install.run(self)

class BuildPy(build_py):
    def run(self):
        self.run_command("build_ext")
        return build_py.run(self)

setup(
    author="Yevgeniy Simonov",
    description="""Test pip installer""",
    name="Test pip installer",
    packages=find_packages(exclude=('tests', 'examples', 'docs')),
    ext_modules=cythonize(
        [
            Extension(
                "pip_installer_test.dummy_program",
                sources=[
                    "pip_installer_test/dummy_program.pyx",
                    "pip_installer_test/src/dummyProgram.cpp"
                ],
                language='c++',
                extra_compile_args=["-w", "-std=c++11"],
                include_dirs=["pip_installer_test"],
                define_macros = [('MAJOR_VERSION', '1'), ('MINOR_VERSION', '0')]
            )
        ], 
        language_level = "3",
        annotate=False,  # this flag if set to true generates html annotation
        nthreads=4,
        build_dir='pip_installer_test'
    ),
    # cmdclass={
    #     'build_ext': BuildExt,
    #     'install': Install,
    # },
    cmdclass={
        'build_py': BuildPy
    }
    setup_requires=[
        'setuptools >= 18.0',
        'cython'
    ],
    zip_safe=True,
    include_dirs=['pip_installer_test']
)   