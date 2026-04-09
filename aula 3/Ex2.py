# a = 'Hoje tem aula!'
# t = len(a)
# print(a[-1])
# #    [ : 8] [8 : ]
# #    [ 1 : 10 : 2 ]
# print(a[5:8])

#1
# nome = input("nome: ")
# print(len(nome), nome[0])

#2
palavra = input("digite uma palavra")
# print(palavra [ 1: :2])
# #3
# print(palavra[: :2])
# #4
# p = input("primeira")
# p2 = input("segunda")
# print(p[1:] + p2 [1:])
#5

invert = palavra[::-1]
print(invert)
if invert == palavra:
    print("é um palíndromo")
else:
    print("não é um alíndromo")
