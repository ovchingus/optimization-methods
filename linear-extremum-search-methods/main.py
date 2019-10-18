from dichotomy import dichotomy
from golden_section import golden_section
from fibonacci import fibonacci
from line_search import line_search
from math import pi, cos


# 3 variant
def function3(x):
    return (x - 2) ** 2


var3 = [function3, -2.0, 20.0]


# 2 variant 
def function2(x):
    return cos(x)


var2 = [function2, 0.0, pi]

func, a, b = var3
tolerancy = 1e-5
max_iterations = 100

print('Dichotomy: ')
print(dichotomy(func, a, b, tolerancy, max_iterations))

print('Line search: ')
print(line_search(func, 0.001))

print('Golden section: ')
print(golden_section(func, a, b, tolerancy, max_iterations))

print('PHIBONACCI FUCK HARD: ')
print(fibonacci(func, a, b, tolerancy, max_iterations))
