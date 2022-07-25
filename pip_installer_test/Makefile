PACKAGENAME=Cython
PYTHON?=python3

# to build all cython files, run: make cython-build

dir1 := .
dir2 := pip_installer_test

clean-all:
	rm -f $(addsuffix /*.c,$(dir2))
	rm -f $(addsuffix /*.html,$(dir2))
	rm -f $(addsuffix /*.so,$(dir2))
	rm -f $(addsuffix /*.pyd,$(dir2))
	rm -f $(addsuffix /*.py[co],$(dir2))

.PHONY: cython-build
cython-build: clean-all
	${PYTHON} $(addsuffix /setup.py,$(dir1)) build_ext --build-lib $(addsuffix /,$(dir2))
	rm -f $(addsuffix /dummy_program.cpp,$(dir2))
