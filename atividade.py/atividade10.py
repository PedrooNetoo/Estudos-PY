def media (num1 , num2):
    resultadoMedia = (num1 + num2) / 2
    print(resultadoMedia)

def diferenca (num1, num2):
    if num1 > num2:
        print(num1 - num2)
    else:
        print(num2 - num1)

def multiplicacao (num1 , num2):
    resultadoMultiplicacao = num1 * num2
    print(resultadoMultiplicacao)

def divisao (num1 , num2):
    resultadoDivisao = num1 / num2
    print(resultadoDivisao)


num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
codigo = int(input("Digite o codigo: "))    

if codigo == 1:
    media (num1, num2)
elif codigo == 2:
    diferenca (num1, num2)
elif codigo == 3:
    multiplicacao (num1, num2)
elif codigo == 4:
    divisao (num1, num2)
else:
    print("Opção Invalida!")

