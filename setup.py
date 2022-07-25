import os
import sys
import subprocess
from setuptools import setup
from setuptools.command.build_ext import build_ext
from setuptools.command.install import install

# python3 setup.py build_ext --inplace

class Install(install):
    def run(self):
        command = ["make", "cython-build"]
        process = subprocess.Popen(command, shell=True, cwd='dummy_program')
        process.wait()
        install.run(self)

setup(
    author="Yevgeniy Simonov",
    author_email="yevgeniy.simonov@theugroup.co",
    description="Dummy Test",
    packages=['dummy_program'],
    has_ext_modules=lambda: True,
    cmdclass={'install': Install}
)