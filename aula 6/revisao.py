

def metodo(metodo, inicio, fim):
    cont = -1
    a = 0
    if metodo == "while":
        while inicio <= fim:
            a = a + inicio
            inicio = inicio + 1
            cont = cont + 1
        media = a / cont
        return a, media
    elif metodo == 'for':
        for i in range(inicio, fim + 1):
            cont = cont + 1
            a = a + i

        media = a / cont
        return  a, media
    else:
        return 0

b = metodo('for',0,2)
print(b)



