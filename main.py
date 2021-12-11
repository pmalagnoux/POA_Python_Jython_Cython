
#import pyximport ; pyximport.install()
import timeit
import time

# "python setup.py build_ext --inplace" before executing this file

if __name__ == '__main__':

    plotting = True

    ######################
    # Fonction Fibonacci #
    ########d#############
    fibo_setup = "import fibonacci_cy"
    fibo_code = '''fibonacci_cy.fib_cdef(30)'''

    print(timeit.timeit(setup=fibo_setup,
                        stmt=fibo_code,
                        number=1000,))


    ######################
    # Allocation tableau #
    ########d#############
    tableau_setup = "import tableaux_cy"
    tableau_code = '''tableaux_cy.alloc_tableaux_cy(1000)'''
    print(timeit.timeit(setup=tableau_setup, stmt=tableau_code, number=1000))

    ######################
    # Fonction factoriel #
    ########d#############
    import factoriel_cy
    bench_start = time.time()
    factoriel_cy.fact_cy(1000000000)
    bench_stop = time.time()

    print "Cython: %s ms" % ((bench_stop - bench_start) * 1000)

