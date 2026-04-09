# nota = int(input("Digite sua nota: "))

# if nota >= 90:
#     print("A")
# else:
#     if nota >= 70:
#         print("B")
#     else:
#         if nota >= 50:
#             print("C")
#         else:
#             print("D")
#
# if nota >= 90:
#     print("A")
# elif nota >= 70:
#     print("B")
# elif nota >= 50:
#     print("C")
# else:
#     print("D")

#EX 1
# numero1 = float(input("Digite o primeiro numero: "))
# op = input("qual operção?:"
#            "(-)  (+)  (*)  (/)")
# numero2 = float(input("Digite o segundo numero: "))

# res = 0
# if op == "-":
#    res =numero1 - numero2
# elif op == "+":
#     res =numero1 + numero2
# elif op == "*":
#     res =numero1 * numero2
# elif op == "/":
#     res =(numero1 / numero2
# else:
#     res ="operação invalida"
# print(res)
    #EX 2

msg = """
----------------------------------------
Preço por tipo e faixa de consumo
----------------------------------------
Tipo        | Faixa (kWh)      | Preço
========================================
Residencial | Até 500          | 0,40
            | Acima de 500     | 0,65
----------------------------------------
Comercial   | Até 1000         | 0,55
            | Acima de 1000    | 0,60
----------------------------------------
Industrial  | Até 5000         | 0,55
            | Acima de 5000    | 0,60
----------------------------------------
"""
quantKwh = float(input("Quantidade de kWh: "))
tipo = input("""
Tipo :
Residencial  ( R )
Comercial    ( C )
Industrial   ( I )
""")
preco = 0
if tipo == 'R':
    if quantKwh <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == 'C':
    if quantKwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == 'I':
    if quantKwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print("opcção inválida")

print(quantKwh * preco)

print(msg)