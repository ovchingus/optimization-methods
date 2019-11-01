import math
from util import gr

'''python program for golden section search.  This implementation
   does not reuse function evaluations and assumes the minimum is c
   or d (not on the edges at a or b)'''


def golden_section(f, a, b, tolerance=1e-5, max_iterations=100):
    """
    golden section search
    to find the minimum of f on [a,b]
    f: a strictly unimodal function on [a,b]

    example:
    >>> f = lambda x: (x-2)**2
    >>> x = gss(f, 1.0, 5.0)
    >>> x
    2.000009644875678

    """

    iteration = 0
    c = b - (b - a) / gr
    d = a + (b - a) / gr

    while iteration < max_iterations:
        iteration += 1

        if abs(c - d) < tolerance:
            return (b + a) / 2

        if f(c) < f(d):
            b = d
        else:
            a = c

        # we recompute both c and d here to avoid loss of precision which may lead to incorrect results or infinite loop
        c = b - (b - a) / gr
        d = a + (b - a) / gr
    return 'Method error, max iterations exceeded'
