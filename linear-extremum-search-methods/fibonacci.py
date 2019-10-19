from math import sqrt
from .util import better_fib


def fibonacci(func, a, b, tol=1e-5, max_iterations=100):
    """
    fibonacci search
    to find the minimum of f on [a,b]
    f: a strictly unimodal function on [a,b]

    example:
    >>> f = lambda x: (x-2)**2
    >>> x = fibonacci(f, -2.0, 20.0)
    >>> x
    2.0

    """
    iteration = 0

    c = .5 * (3.0 - sqrt(5.0))
    d = 0.0

    # 1.1102e-16 is machine precision
    eps = 1.2e-16
    eps = sqrt(eps)

    v = a + c * (b - a)
    w = v
    x = v
    e = 0.0
    fx = func(x)
    fv = fx
    fw = fx
    tol3 = tol / 3.0

    xm = .5 * (a + b)
    tol1 = eps * abs(x) + tol3
    t2 = 2.0 * tol1

    # main loop
    while abs(x - xm) > (t2 - .5 * (b - a)):
        iteration += 1
        if iteration > max_iterations:
            return 'Method error, max iterations exceeded'

        p = q = r = 0.0
        if abs(e) > tol1:
            # fit the parabola
            r = (x - w) * (fx - fv)
            q = (x - v) * (fx - fw)
            p = (x - v) * q - (x - w) * r
            q = 2.0 * (q - r)

            if q > 0.0:
                p = -p
            else:
                q = -q

            r = e
            e = d

        if abs(p) < abs(.5 * q * r) and q * (a - x) < p < q * (b - x):
            # a parabolic interpolation step
            d = p / q
            u = x + d
            # f must not be evaluated too close to a or b
            if (u - a) < t2 or (b - u) < t2:
                d = tol1
                if x >= xm:
                    d = -d
        else:
            # a golden-section step
            if x < xm:
                e = b - x
            else:
                e = a - x
            d = c * e

        # f must not be evaluated too close to x
        if abs(d) >= tol1:
            u = x + d
        else:
            if d > 0.0:
                u = x + tol1
            else:
                u = x - tol1

        fu = func(u)

        # Update a, b, v, w, and x
        if fx <= fu:
            if u < x:
                a = u
            else:
                b = u

        if fu <= fx:
            if u < x:
                b = x
            else:
                a = x

            v = w
            fv = fw
            w = x
            fw = fx
            x = u
            fx = fu

            xm = .5 * (a + b)
            tol1 = eps * abs(x) + tol3
            t2 = 2.0 * tol1
        else:
            if fu <= fw or w == x:
                v = w
                fv = fw
                w = u
                fw = fu

                xm = .5 * (a + b)
                tol1 = eps * abs(x) + tol3
                t2 = 2.0 * tol1
            elif fu > fv and v != x and v != w:
                xm = .5 * (a + b)
                tol1 = eps * abs(x) + tol3
                t2 = 2.0 * tol1
            else:
                v = u
                fv = fu

                xm = .5 * (a + b)
                tol1 = eps * abs(x) + tol3
                t2 = 2.0 * tol1
    return x
