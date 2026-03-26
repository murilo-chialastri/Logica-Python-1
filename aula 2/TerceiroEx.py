# a = int(input("valor de A "))
# b = int(input("valor de B "))
#
# if a > b:
#     print("A é maior que B")
#     print(a)
# else:
#     print("B é maior que A")
#     print(b)
#
# velocidade = int(input("velocida do carro "))
# if velocidade > 80:
#     print("você foi multado ")
#     multa = 5 * (velocidade - 80)
#     print("valor da multa:", multa, "reais")
# else:
#     print("parabéms")

# sal = float(input("salario: "))
# if sal > 1250.00:
#     aumento = sal + sal * 0.1
#     print("aumento ", aumento)
# else:
#     aumento = sal + sal * 0.15
#     print("aumento ", aumento)

# n1 = int(input("escreva um numero1 "))
# n2 = int(input("escreva um numero2 "))
# n3 = int(input("escreva um numero3 "))
#
# if n1 > n2 and n1 > n3 :
#     print(n1)
#     if n2 > n3:
#         print(n3)
#     else:
#         print(n2)
# elif n2 > n1 and n2 > n3:
#     print(n2)
#     if n1 > n3:
#         print(n3)
#     else:
#         print(n1)
# elif n3 > n1 and n3 > n2:
#     print(n3)
#     if n1 > n2:
#         print(n2)
#     else:
#         print(n1)

f = float(input("numero"))
if f % 2 == 0 and f > 100:
    print("a")