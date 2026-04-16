# num = int(input("digite um numero"))
# n = 1
# while(n <= num):
#     if n % 2 == 0:
#         print(n)
#     n += 1

# num = int(input("digite um numero"))
# n = 1
# while(n <= num):
#     if n % 2 != 0:
#         print(n)
#     n += 1

# num = int(input("digite um numero"))
# n = 1
# p = 0
# while(n <= num):
#     if n % 2 == 0:
#         p = p + n
#     n += 1
#
# print(p)
soma = 0
while(True):
    opc = int(input("Digite um número (0 para parar): "))
    soma += opc
    if opc == 0:
        break
print(soma)