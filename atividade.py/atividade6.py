def verificarMaior(num1 , num2):
    if num1 > num2:
        print("num1 maior que num2")
    elif num2 > num1:
        print("num2 maior que num1")
    else:
        print("Os dois numeros são iguais")

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
verificarMaior(num1 , num2)
