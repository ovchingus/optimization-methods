from decimal import Decimal
from math import (
    sqrt,
)

from funcion import (
    a,
    b,
    epsilon,
    calculate_function,
    print_information,
    find_a_b
)


def calculate_fibonacci(n):
    return Decimal(((1+sqrt(5)/2)**n)/sqrt(5))


def calculate_x(a, b, n):

    fib_n = calculate_fibonacci(n)
    fib_1n = calculate_fibonacci(n+1)
    fib_2n = calculate_fibonacci(n+2)

    return a+fib_n/fib_2n*(b-a), a+fib_1n/fib_2n*(b-a)


n = 0
while b - a > epsilon:
    x1, x2 = calculate_x(a, b, n)
    n += 1

    y_x1 = calculate_function(x1)
    y_x2 = calculate_function(x2)

    b_previous, a_previous = b, a

    a, b = find_a_b(a, b, x1, x2, y_x1, y_x2)

    context = (
        str(n).ljust(4, ' '),
        a_previous, b_previous,
        a, b,
        (b_previous - a_previous) / (b - a),
        x1, y_x1,
        x2, y_x2
    )

    print_information(context)

print("\n\n%.5f %.5f %s" % (a, b, n))