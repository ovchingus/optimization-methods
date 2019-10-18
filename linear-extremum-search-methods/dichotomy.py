import util

def dichotomy(fun, left, right, tolerance, max_iterations = 100):
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
    # iteration = 0
    a = 0.0
    b = 2.0
    while b - a > tolerance:
        c = (a + b) / 2
        if fun(b) * fun(c) < 0:
            a = c
        else:
            b = c
    return (a + b) / 2

