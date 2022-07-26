from setuptools import setup, find_packages, Extension
from setuptools.command.build_py import build_py as _build_py    
from Cython.Build import cythonize
import subprocess
import os

path = os.path.dirname(os.path.realpath(__file__))

class build_py(_build_py):
    def run(self):
        # self.run_command("build_ext")
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
    cmdclass = {'build_py' : build_py}
)