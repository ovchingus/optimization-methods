from math import cos, pi
from decimal import Decimal


def find_a_b(a, b, x1, x2, y_x1, y_x2):
    return (a, x2) if y_x1 > y_x2 else (x1, b)


def calculate_function(x):
    return (x - 2) ** 2


a, b = Decimal(-2.0), Decimal(20.0)
epsilon = 1e-5
