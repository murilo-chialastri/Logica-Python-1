
#  PEGAR CPF
cpf = input("digite cpf: ") #cpf = 11
digito = cpf[9:] # PEGA 2 ULTIMOS DIGITOS
#p1 = cpf[9]

#print(digito) #
if len(cpf) == 11:
    # PRIMEIRO NUMERO
    conta1 = (int(cpf[0]) * 10 + int(cpf[1]) * 9 + int(cpf[2]) * 8 + int(cpf[3]) * 7 + int(cpf[4]) * 6
                                                + int(cpf[5]) * 5 + int(cpf[6]) * 4 + int(cpf[7]) * 3 + int(cpf[8]) * 2  )%11
    digito1 = 0
    if conta1 < 2:
        digito1 = 0
    else:
        digito1 = 11 - conta1
    #----------------------------------------------------------------------------------------------------------------------------------
    #SEGUNDO NUMERO
    conta2 = (  int(cpf[0]) * 11 + int(cpf[1]) * 10 + int(cpf[2]) * 9 + int(cpf[3]) * 8 + int(cpf[4]) * 7
                                                + int(cpf[5]) * 6 + int(cpf[6]) * 5 + int(cpf[7]) * 4 + int(cpf[8]) * 3 + digito1 * 2 )%11
    digito2 = 0
    if conta2 < 2:
        digito2 = 0
    else:
        digito2 = 11 - conta2
    #----------------------------------------------------------------------------------------------------------------------------------

    # Válidador de CPF
    if digito == str(digito1) + str(digito2):
        print("CPF Válido")
    else:
        print("CPF incorreto")

else:
    print("CPF incorreto!")