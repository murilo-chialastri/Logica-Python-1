# print("""++
# ||
# ++""")
# print('-' * 10)

def geradorDeRetangulo(linhas, colunas):
    borda = '+'
    linha = '-'
    coluna = '|'
    print(f'''{borda}{linha * linhas}{borda}''')
    for c in range(colunas):
        print(f'''{coluna}{linha * linhas}{coluna}''')
    print(f'''{borda}{linha * linhas}{borda}''')

geradorDeRetangulo(4, 3)

while(True):
    linhas = int(input('Digite o tamanho da linha: '))
    if linhas > 20 or linhas < 1:
        print('a linha deve ter no mínimo 1 e no máximo 20')
    else:
        colunas = int(input('Digite o tamanho da coluna: '))
        if colunas > 20 or colunas < 1:
            print('a coluna deve ter no mínimo 1 e no máximo 20')
        else:
            geradorDeRetangulo(linhas, colunas)
            break



