# def maior (x, y):
#     if x >= y:
#         return x
#     else:
#         return y
#
# a = maior(102,12)
# print(a)
#
# def parOuImpar(x):
#     if x % 2 == 0:
#         return 'P'
#     elif x <= 0:
#         return 'F'
#     else:
#         return 'N'
#
# b = parOuImpar(-23)
# print(b)
#
# def mult(x,y):
#     if x % y == 0:
#         return True
#     else:
#         return False
#
# c = mult(12,2)
# print(c)
#
# def area (x, y):
#     if x > 0 and y > 0:
#         return x * y
#     else:
#         return None
#
# d = area(10, 2)
# print(d)

def pi (x):
    y = 0
    l = doisEmDois(x)
    res =0
    for i in range(1,x+1):

        b = troca(i)



        print(f'{res} =+ {b}/{l[y]}')
        res +=  b / l[y]
        y += 1
    return res

def troca(y):
    if y % 2 == 0:
        return -1
    else:
        return +1


def doisEmDois(z):
    lista = []
    for i in range(1,z*2+1,2):
        lista.append(i)

    return lista




l = doisEmDois(2)
# print(l[3])

print(pi(220) * 4)