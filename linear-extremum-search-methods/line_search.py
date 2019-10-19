def line_search(fun, tolerance, max_iterations=100):
    iteration = 0
    x0 = 0
    h = 0
    xk = 0
    x_next = float('-inf')
    x_prev = 0

    if fun(x0) > fun(x0 + tolerance):
        xk = x0 + tolerance
        h = tolerance
    elif fun(x0) > fun(x0 - tolerance):
        xk = x0 - tolerance
        h = -tolerance

    while iteration < max_iterations:
        h *= 2
        x_next = xk + h
        if fun(xk) > fun(x_next):
            x_prev = xk
            xk = x_next
        iteration += 1
    return x_prev, x_next

