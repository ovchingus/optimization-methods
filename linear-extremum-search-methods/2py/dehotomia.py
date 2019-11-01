from decimal import Decimal

from funcion import (
    a,
    b,
    epsilon,
    calculate_function,
    find_a_b,
    print_information
)


def calculate_x(a, b, epsilon):
    return ((a+b)+epsilon)/Decimal(2), ((a+b)-epsilon)/Decimal(2)


n = 0
while b - a > epsilon+epsilon/100000:
    x1, x2 = calculate_x(a, b, epsilon)
    n += 1

    y_x1 = calculate_function(x1)
    y_x2 = calculate_function(x2)

    b_previous, a_previous = b, a

    a, b = find_a_b(a, b, x1, x2, y_x1, y_x2)

    context = (
        str(n).ljust(4, ' '),
        a_previous, b_previous,
        a, b,
        (b_previous-a_previous)/(b - a),
        x1, y_x1,
        x2, y_x2
    )

    print_information(context)


print("%.5f %.5f %s" % (a, b, n))