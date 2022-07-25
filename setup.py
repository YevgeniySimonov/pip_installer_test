import os
import sys
import subprocess
from setuptools import setup
from setuptools.command.build_ext import build_ext
from setuptools.command.install import install
from setuptools.command.build_py import build_py
from setuptools.command.build_clib import build_clib

# python3 setup.py build_ext --inplace

class Install(install):
    def run(self):
        command = ["make", "cython-build"]
        process = subprocess.Popen(command, shell=True, cwd='dummy_program')
        process.wait()
        install.run(self)

class BuildExt(build_ext):
    """Customized setuptools build_ext command - builds protos on build."""
    def run(self):
        protoc_command = ["make", "cython-build"]
        if subprocess.call(protoc_command) != 0:
            sys.exit(-1)
        build_ext.run(self)

class BuildClib(build_clib):
    """Customized setuptools build_clib command - builds protos on build."""
    def run(self):
        protoc_command = ["make", "cython-build"]
        if subprocess.call(protoc_command) != 0:
            sys.exit(-1)
        build_clib.run(self)

class BuildPy(build_py):
    """Customized setuptools build_py command - builds protos on build."""
    def run(self):
        protoc_command = ["make", "cython-build"]
        if subprocess.call(protoc_command) != 0:
            sys.exit(-1)
        build_py.run(self)
    
setup(
    author="Yevgeniy Simonov",
    author_email="yevgeniy.simonov@theugroup.co",
    description="Dummy Test",
    packages=['pip_installer_test'],
    has_ext_modules=lambda: True,
    cmdclass={
        # 'install': Install,
        'build_ext': BuildExt
        # 'build_clib': BuildClib
        # 'build_py': BuildPy
    }
)