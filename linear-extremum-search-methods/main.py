from dichotomy import dichotomy
from golden_section import golden_section
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

print('Dichotomy: \n')
print(dichotomy(func, a, b, 1e-5, 5))

print('Golden section: \n')
print(golden_section(func, a, b, 1e-5, 5))

