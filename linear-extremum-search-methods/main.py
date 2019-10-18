import dichotomy

# 3 variant
def function3(x):
    return (x - 2) ** 2

a = -2.0
b = 20.0


print(dichotomy.dichotomy(function3, a, b, 0.01, 100))


