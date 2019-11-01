from numpy import array
from math import sqrt

from funcion import (
    calculate_function_2,
    epsilon
)


def calc_f(x1, x2):
    return -4*x1*(-x1**2+x2)+2*x1-2


def calc_g(x1, x2):
    return -2*x1**2+2*x2

def return_func(x1, x2):
    fun_1 = calc_f(x1, x2)
    fun_2 = calc_g(x1, x2)

    ee = sqrt(fun_1**2 + fun_2**2)

    if ee != 0:
        fun_1 /= ee
        fun_2 /= ee

    return [fun_1, fun_2]



lamb = 1


x_prev = array([2,2])
y_prev = calculate_function_2(*x_prev)

while True:
    lamb_temp = lamb
    x_new = x_prev - array(return_func(*x_prev))*lamb
    y_new = calculate_function_2(*x_new)

    if lamb <= epsilon:
        break
    elif y_prev < y_new:
        lamb = lamb/2
    else:
        x_prev = x_new
        y_prev = y_new
        lamb = lamb_temp

    print(x_prev, x_new, y_prev, y_new, lamb)


    print("%s %s" % (x_prev, x_new))