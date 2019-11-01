from decimal import Decimal

from funcion import (
    a,
    b,
    epsilon,
    calculate_function,
    print_information
)


def calculate_x(a, b):

    return a + golden_section_coefficient * (b - a), \
           b - golden_section_coefficient * (b - a)


def find_a_b(y_x1, y_x2, a, b):
    return (a, x2) if y_x1 < y_x2 else (x1, b)


golden_section_coefficient = Decimal(0.381966011)

n = 0
while b - a > epsilon:
    x1, x2 = calculate_x(a, b)
    n += 1

    y_x1 = calculate_function(x1)
    y_x2 = calculate_function(x2)

    b_previous, a_previous = b, a

    a, b = find_a_b(y_x1, y_x2, a, b)

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