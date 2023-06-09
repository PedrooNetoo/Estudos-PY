def calculadora(num1, num2, simbolo):
    if simbolo == '+':
        resultado = num1 + num2
        print(resultado)
    elif simbolo == '-':
        resultado = num1 - num2
        print(resultado)
    elif simbolo == '*':
        resultado = num1 * num2
        print(resultado)
    elif simbolo == '/':
        resultado = num1 / num2
        print(resultado)
    else:
        print("Simbolo inválido!")
        

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
simbolo = input("Digite o operador (+, -, *, /): ")

calculadora(num1, num2, simbolo)
