import util

def dichotomy(fun, left, right, tolerance, max_iterations = 100):
    """
    INPUT: Function fun, 
            endpoint values left, right, 
            tolerance, 
            maximum iterations max
    CONDITIONS: 
            left < right, 
            either f(left) < 0 and f(right) > 0 or f(left) > 0 and f(right) < 0
    OUTPUT: value which differs from a root of f(x) = 0 by less than tolerance
    """
    iteration = 0
    while iteration < max_iterations: # limit iterations to prevent infinite loop
        mid = (left + right) / 2 # new midpoint
        if fun(mid) == 0 or (right - left) < tolerance: # solution found
            return mid
        iteration += 1
        if fun(right) * fun(mid) < 0: # new interval
            left = mid
        else: 
            right = mid

    print('Method failed, max number of steps exceeded.')
    return None

# dichotomy()

