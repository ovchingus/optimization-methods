import numpy as np
from numpy.linalg import norm
from scipy.constants import golden

def f(x):
     return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2

def theory_gradient(x1, x2):
    derivative_x1 = -400 * x1 * (x2 - x1**2) + 2 * x1 - 2
    derivative_x2 = -200 * x1**2 + 200 * x2
    
    return np.array([derivative_x1, derivative_x2])

# Метод двусторонней разности
def numerical_gradient(x1, x2, dx = 1e-6):
    derivative_x1 = (f([x1 + dx, x2]) - f([x1 - dx, x2])) / (2*dx)
    derivative_x2 = (f([x1, x2 + dx]) - f([x1, x2 - dx])) / (2*dx)
    
    return np.array([derivative_x1, derivative_x2])

def golden_ratio(f, a, b, e, grad, x):
    t = golden - 1
    x1_n = a + (1 - t) * (b - a)
    x2_n = a + t * (b - a)
    f1_n = f(x - x1_n * grad)
    f2_n = f(x - x2_n * grad)
    e_n = (b - a) / 2
    
    while True:   
        if e_n <= e:
            return (b + a) / 2
        
        if f1_n <= f2_n:
            b = x2_n
            x2_n = x1_n
            f2_n = f1_n
            x1_n = a + (1 - t) * (b - a)
            f1_n = f(x - x1_n * grad)
        else:
            a = x1_n
            x1_n = x2_n
            f1_n = f2_n
            x2_n = a + t * (b - a)
            f2_n = f(x - x2_n * grad)
        e_n = t * e_n

def find_on_straight(f, x0, grad, x_, sigma = 0.0001):
    if f(x_ - x0 * grad) > f(x_ - (x0 + sigma) * grad):
        x = x0 + sigma
        h = sigma
    else:
        x = x0 - sigma
        h = -sigma
    while True: 
        h *= 2
        x_next = x + h

        if f(x_ - x * grad) > f(x_ - x_next * grad):
            x = x_next
        else:
            return [x - h / 2, x_next]

def gradient_descent(f, gradient, x, e = 0.001, limit = 5000):
    nit = 0
    x_min = x.copy()
    
    for i in range(0, 5):
        j = 0
        x = x + np.array([30 * i * (-1)**i] * len(x))
        grad = gradient(x[0], x[1])
        grad = grad / norm(grad)
        borders = find_on_straight(f, 0, grad, x)
        h = golden_ratio(f, borders[0], borders[1], e = 0.0000001, grad = grad, x = x)
        
        while norm(gradient(x[0], x[1])) > e and j < limit:
            j += 1
            borders = find_on_straight(f, 0, grad, x)
            h = golden_ratio(f, borders[0], borders[1], e = 0.0000001, grad = grad, x = x)
            x = x - h * grad
            grad = gradient(x[0], x[1])
            grad = grad / norm(grad)
            nit += 1
            
        if(f(x_min) > f(x)):
                x_min = x.copy()
        
    return (x_min, nit)

print(gradient_descent(f, theory_gradient, [100, 100], e = 0.001))

count = np.array([0])

def wrap_f(x):
    count[0] += 1
    return f(x)

def wrap_theory_gradient(x1, x2):
    count[0] += 2
    return theory_gradient(x1, x2)

def wrap_numerical_gradient(x1, x2):
    count[0] += 2
    return numerical_gradient(x1, x2)

iters = []
counts = []
errors = []
x1 = []
x2 = []

for e in np.arange(0.001, 0.02, 0.001):
    count[0] = 0
    res = gradient_descent(wrap_f, wrap_theory_gradient, [0, 0], e = e)
    counts.append(count[0])
    iters.append(res[1])
    errors.append(e)
    x1.append(res[0][0])
    x2.append(res[0][1])

print(iters, counts, errors, x1, x2)

iters = []
counts = []
errors = []
x1 = []
x2 = []

for e in np.arange(0.001, 0.02, 0.001):
    count[0] = 0
    res = gradient_descent(wrap_f, wrap_numerical_gradient, [0, 0], e = e)
    counts.append(count[0])
    iters.append(res[1])
    errors.append(e)
    x1.append(res[0][0])
    x2.append(res[0][1])

print(iters, counts, errors, x1, x2)