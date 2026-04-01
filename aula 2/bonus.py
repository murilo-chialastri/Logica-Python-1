nome = input("digite seu nome ")
print("olá", nome)

velocidade = float(input("qual é a sua velocidade? "))
limite = 110
if velocidade > 110:
    multa = (velocidade - 110) * 5
    print("você foi multado em",multa,"reais")
    metodo = int(input("como você deseja pagar?"
                       "\nDigite (1) para pagamento no crédito (taxa 10%)"
                       "\nDigite (2) para pagamento no Pix (desconto 15%)\n:"))
    if metodo == 1:
        pagar = multa * 0.1 + multa
    elif metodo == 2:
        pagar = multa - multa * 0.15
    else:
        print("método inválido")
        
    print("Valor a pagar", pagar,"\nObrigado!",nome)
else:
    print("Muito bem
