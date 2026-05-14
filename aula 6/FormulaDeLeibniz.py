def pi(x):
    j = 0
    l = doisEmDois(x)
    res = 0
    for i in range(1, x + 1):
        pOuN = troca(i)
        print(f'{res} =+ {pOuN}/{l[j]}')
        res += pOuN / l[j]
        j += 1
    return res


def troca(y):
    if y % 2 == 0:
        return -1
    else:
        return +1


def doisEmDois(z):
    lista = []
    for i in range(1, z * 2 + 1, 2):
        lista.append(i)
    return lista





print(pi(2203) * 4)