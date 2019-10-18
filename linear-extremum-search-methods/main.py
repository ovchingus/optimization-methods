from dichotomy import dichotomy
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

#print(dichotomy(func, a, b, 0.001, 5))

print(line_search(func, 0.001))
