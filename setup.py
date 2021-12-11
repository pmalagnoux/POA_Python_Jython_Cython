from setuptools import setup
from Cython.Build import cythonize

setup(
   ext_modules = cythonize(["fibonacci_cy.pyx",
                            "tableaux_cy.pyx",
                            "factoriel_cy.pyx"])
)
