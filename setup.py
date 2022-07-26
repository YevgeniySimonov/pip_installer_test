from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext 
from Cython.Build import cythonize
import subprocess
import os

path = os.path.dirname(os.path.realpath(__file__))

class Build(build_ext):
    def run(self):
        subprocess.check_call(['make', 'cython-build'], cwd=path)
        return super().run()

setup(
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
                include_dirs=["pip_installer_test"]
            )
        ],
        language_level="3",
        build_dir='pip_installer_test/'
    ),
    cmdclass = {'build_ext' : Build}
)