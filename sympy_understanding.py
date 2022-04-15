"""The following program uses the sympy module to explain the basic mathematical operations that can be performed. The
following program can be used to understand the basics of integrals and few operations that is routinely done on
matrices.
Understand the basics of integrals with the visual of the function along with the integral values.
"""

import sympy as sp
from sympy import *
from sympy import Symbol, sin, cos, tan, cot, csc, sec, exp, shape
from sympy.plotting import plot
from sympy.integrals.trigonometry import trigintegrate
from sympy.abc import y

#Function created to integrate algebraic functions with x as the variable
def algebraic():
    x = sp.Symbol('x')
    final_integral_value = sp.integrate((x**2 + 3*x + 5), x)
    print(f"The integral value is {final_integral_value}")
    p1 = plot((x**2 + 3*x + 5))

#Function created to integrate trignometric functions with y as the variable
def trignometric():
    trig_function = cos(y)
    trig_integral_value = trigintegrate(trig_function, y)
    print(f"The integral value is {trig_integral_value}")
    p2 = plot(trig_function)

#Function created to validated different matrix operations
def matrixoperations():
    matrix1 = Matrix([[1, 2, 3], [1, 2, 3], [3, 4, 5]])
    print(f"Matrix1 = {matrix1}\n")
    check_dim = shape(matrix1)
    print(f"Matrix1 dimensions are {check_dim}\n")
    matrix2 = Matrix([[5, 6, 1], [8, 9, 2], [1, 2, 3]])
    print(f"Matrix2 = {matrix2}\n")
    check_dim2 = shape(matrix2)
    print(f"Matrix2 dimensions are {check_dim2}\n")
    matrix3 = matrix1 * matrix2
    print(matrix3)
    check_dim3 = shape(matrix3)
    print(f"The final matrix dimension is {check_dim3}\n")


#Call the functions that you would like to visualise
trignometric()


