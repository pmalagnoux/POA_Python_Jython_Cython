import random
from libc.stdlib cimport malloc, free

def alloc_tableaux_cy(int size):
    return alloc_tableaux(size)

cdef void alloc_tableaux(int size):
    cdef int i
    cdef double *my_array = <double *> malloc(size * sizeof(double))
    if not my_array:
        raise MemoryError()

    try:
        ran = random.normalvariate
        for i in range(size):
            my_array[i] = ran(0, 1)

    finally:
        # return the previously allocated memory to the system
        free(my_array)