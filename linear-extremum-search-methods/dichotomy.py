def dichotomy(f, a, b, tolerance=1e-5, max_iterations=100):
    """
    dichotomy search
    to find the minimum of f on [a,b]
    f: a strictly unimodal function on [a,b]

    example:
    >>> f = lambda x: (x-2)**2
    >>> x = dichotomy(f, -2.0, 20.0)
    >>> x
    1.99999880791

    """
    iteration = 0
    while iteration < max_iterations:
        iteration += 1

        mid = (a + b) / 2

        if abs(b - a) <= tolerance:
            return mid

        f1 = f(mid - tolerance)
        f2 = f(mid + tolerance)

        if f1 < f2:
            b = mid
        else:
            a = mid

    return 'Method error, max iterations exceeded'
