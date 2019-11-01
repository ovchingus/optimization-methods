from decimal import Decimal


from funcion import calculate_function

x0 = Decimal(0)
y_x0 = calculate_function(x0)

eps = Decimal(0.2)

epsilon = eps if y_x0 > calculate_function(x0+eps) else -eps
h = epsilon * 2

while True:
    x1 = x0+h
    y_x1 = calculate_function(x1)

    if y_x0 > y_x1:
        y_x0 = y_x1
    else:
        break


    h *= 2

print("%s %s" % (x0, x1))