import time

# variaveis
menu = """
        interface
+-------------------------+
|                  ______ |
|               2 |filtro||
|                  ------ |
|                         |
|  ______          ______ |
|1| foto |       3|salvos||
|  ------          ------ |
|            0            |
|        finalizar        |
+-------------------------+
Opção: """
foto = ""
op = -1
fotosSalvas = []

# Funções
def tirarFotos():
    foto = input("nome da foto")
    fotosSalvas.append(foto)
def msgFotos():
    print("tirando foto.")
    time.sleep(0.4)
    print("tirando foto..")
    time.sleep(0.4)
    print("tirando foto...")
    time.sleep(0.4)

while(op != 0):
    op = int(input(menu))

    if op == 1:
        while(True):
            msgFotos()
            tirarFotos()
    elif op == 2:
        print()
    elif op == 3:
        for fotos in fotosSalvas:
            print(fotos)







# Adicionar lista que guarda nome das fotos e quantidade de fotos (1)
# opção mudar filtro para auto, sem , salvos (2)
# mostar lista de fotos com nome e quantidade (3)