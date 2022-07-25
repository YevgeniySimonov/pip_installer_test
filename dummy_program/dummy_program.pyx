
cdef extern from "src/dummyProgram.hpp":
    cdef void dummyPrint()

cpdef void dummy_print():
    dummyPrint()
