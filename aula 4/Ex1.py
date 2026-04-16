# x = 18
# nome = "Maria"
# z = "%s tem %d anos" % (nome, x)
# print(z)
from sympy import print_rcode

# %d   %s   %f
#============================================================================

# valor = 12.50
# b = 'O valor do pastel é R$[%5.2f]' % valor
# a= 'o valor do pastel é {}'.format(valor)
# print(a)
# print(b)

# x = 20
# nome = 'maria'
#
# a = f'{nome} tem {x} anos'
#
# valor = 12.50
#
# b = f'0 valor é {valor:.2f}'
#
#
#
#
# print(f'{"":->17s}')
# print(f'|{'Tinto':<6} | {valor:5.2f}|')

nome = input("nome")
idade = int(input('idade'))
escolha = input('qual produto deseja:\n1-pera 6.5 reais\n2-maça 5.2 reais\n3-melão 15.99 reais')

preco = 0
if escolha == '1':
    preco = 6.5
elif escolha == '2':
    preco = 5.2
elif escolha == '3':
    preco = 15.99
else:
    print('escolha inválida')

print(f'Seu nome {nome}, sua idade {idade}, valor da compra R${preco:.2f}')