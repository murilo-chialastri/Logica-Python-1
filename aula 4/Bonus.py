tab = ("Código | Preço\n"
       "  1    |  0,5  \n"
       "  2    |  1,5   \n"
       "  3    |  5,0   \n"
       "  4    |  6,0   \n"
       "  5    |  8,5   \n"
       "")
strQuant = "Quantos vicê deseja comprar? "

totalQuant = 0
total = 0
escolha = -1
while(escolha != 0):
    escolha = int(input(tab))
    if escolha == 1:
        valor = 0.5
        qat = int(input(strQuant))
        totalQuant = valor * qat
    elif escolha == 2:
        valor = 1.5
        qat = int(input(strQuant))
        totalQuant = valor * qat
    elif escolha == 3:
        valor = 5.0
        qat = int(input(strQuant))
        totalQuant = valor * qat
    elif escolha == 4:
        valor = 6.0
        qat = int(input(strQuant))
        totalQuant = valor * qat
    elif escolha == 5:
        valor = 8.5
        qat = int(input(strQuant))
        totalQuant = valor * qat
    total = total + totalQuant

print(total)