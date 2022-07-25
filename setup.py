import os
from Cython.Build import cythonize

try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension

# compile: python3 setup.py build_ext --inplace

path = os.path.dirname(__file__)
defs = [('NPY_NO_DEPRECATED_API', 0)]

print('compillation path: ', path)

extending = Extension(
    "dummy_program",
    sources=[
            os.path.join(path, 'dummy_program.pyx'),
            os.path.join(path, 'dummyProgram.cpp')
        ],
    language='c++',
    extra_compile_args=["-w", "-std=c++11"],
    include_dirs=[
        os.path.join(path, '..', '..')
    ],
    define_macros=defs        
)

extensions = [extending]

setup(
    author="Yevgeniy Simonov",
    description="""Test pip installer""",
    name="Test pip installer",
    ext_modules=cythonize(
        extensions, 
        language_level = "3",
        annotate=False,  # this flag if set to true generates html annotation
        nthreads=4
    ),
    zip_safe=True,
)