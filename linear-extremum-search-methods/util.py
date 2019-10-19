from math import sqrt


def sign(x):
    """
    Return 1 if arg larger then 0, -1 is smaller then 0
    
    """
    return int(x > 0)


gr = (1 + sqrt(5)) / 2


def naive_fib(n):
    if 0 <= n <= 1:
        return n
    else:
        return naive_fib(n - 1) + naive_fib(n - 2)


def better_fib(n):
    if 0 <= n <= 1:
        return n
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]
