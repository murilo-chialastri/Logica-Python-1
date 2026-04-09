cpf = input("digite cpf")
#cpf = 11
digito = cpf[9:]
print(digito)
conta1 = (int(cpf[0]) * 10 + int(cpf[1]) * 9 + int(cpf[2]) * 8 + int(cpf[3]) * 7 + int(cpf[4]) * 6
                                            + int(cpf[5]) * 5 + int(cpf[6]) * 4 + int(cpf[7]) * 3 + int(cpf[8]) * 2  )%11
if conta1 < 2:
    digito1 = 0
else:
    digito = 11 - conta1

conta1 = (int(cpf[0]) * 10 + int(cpf[1]) * 9 + int(cpf[2]) * 8 + int(cpf[3]) * 7 + int(cpf[4]) * 6
                                            + int(cpf[5]) * 5 + int(cpf[6]) * 4 + int(cpf[7]) * 3 + int(cpf[8]) * 2  )%11

print(conta1)
res = int(digito) == conta
print(res)