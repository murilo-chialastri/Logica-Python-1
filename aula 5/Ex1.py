# l = [7.6, 8.4, 10, 4, 5.5, 8]
#
# i = 0
# a = l[2:]
# b = l[:5]
# c = l[::2]
# d = l[::-1]
# e = l[-1]
#
# while i < len(l):
#     print(l[i])
#     i = i + 1

# animais = []
# print(animais)
#
# animais.append('cachorro')
# animais.append('gato')
# animais.append('hamster')
#
# animais.pop()
# print(animais)
opcao = 1
lista =[]
while opcao != 0:
    opcao = int(input("Deseja adicionar(1) ou Atender(2) mostrar (3)"))
    if opcao == 1:
        pessoa = input('nome da pessoa')
        lista.append(pessoa)
    elif opcao == 2:
        lista.pop(0)
        print(lista)
    elif opcao == 3:
        print(lista)
    elif opcao == 0:
        break
    else:
        print("opção inválida")

for i in range(11):
    print(i)