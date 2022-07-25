
cdef extern from "dummyProgram.hpp":
    cdef void dummyPrint()

cpdef void dummy_print():
    dummyPrint()
