def dichotomy(fun, a, b, tolerance, max_iterations=100):
    """
    INPUT: 
        Function fun, 
        endpoint values left, right, 
        tolerance, 
        maximum iterations max
    CONDITIONS: 
        left < right, 
        either f(left) < 0 and f(right) > 0 or f(left) > 0 and f(right) < 0
    OUTPUT: 
        Value which differs from a root of f(x) = 0 by less than tolerance
    """
    iteration = 0
    while iteration < max_iterations:
        mid = (a + b) / 2

        if abs(b - a) <= tolerance:
            return mid

        f1 = fun(mid - tolerance)
        f2 = fun(mid + tolerance)

        print(f1, mid, f2)

        if f1 < f2:
            b = mid
        else:
            a = mid

    return 'Method error, max iterations exceeded'
