a = 2
b = -8
c = 6

def segundGrau(a, b, c):
    delta = b**2 - 4 * a * c #certo
    raizDelta = delta**(1/2)

    x1 = (-b + raizDelta) / (2 * a)
    x2 = (-b - raizDelta) / (2 * a)
    return "delta:",delta,"x1:", x1 ,"x2:", x2

print(segundGrau(a,b,c))