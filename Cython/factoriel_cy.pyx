def fact_cy(int n):
    return c_fact(n)

cdef long c_fact(long n):
    if n <= 1:
        return 1
    return n * c_fact(n-1)
