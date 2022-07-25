import sys
import os
import subprocess
from setuptools import setup
from setuptools.command.build_ext import build_ext

# python3 setup.py build_ext --inplace

print(os.path.dirname(__name__))

class BuildExt(build_ext):
    """Customized setuptools build_ext command - builds protos on build."""
    def run(self):
        protoc_command = ["make", "cython-build"]
        if subprocess.call(protoc_command) != 0:
            sys.exit(-1)
        build_ext.run(self)
    
setup(
    author="Yevgeniy Simonov",
    author_email="yevgeniy.simonov@theugroup.co",
    description="Dummy Test",
    packages=['pip_installer_test'],
    include_dirs=['pip_installer_test/'],
    has_ext_modules=lambda: True,
    cmdclass={'build_ext': BuildExt}
)