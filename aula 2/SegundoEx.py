nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print("Olá meu nome é",nome,"e tenho",idade,"anos")

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

resultado = n1 + n2
print(resultado)

temp = int(input("quantas anos está na empresa: "))
valorPAno = 200
bonus = temp * valorPAno
print("você ganhou um bonus de", bonus)

preco = float(input("preço da mercadoria: "))
percentualDesc = float(input("percentual de desconto "))
prodDesc =  percentualDesc * preco / 100
novoDes = preco - prodDesc
print("O produto custa", novoDes)


quantKM = float(input("quantos km percorreu? "))
diaAlug = int(input("quantos dias ficou alugado? "))
carroPreco = 60 * diaAlug
precoKm = quantKM * 0.15
totalApagar = carroPreco + precoKm
print("total a pagar: ", totalApagar)