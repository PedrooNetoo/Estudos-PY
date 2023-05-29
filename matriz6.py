valores = [0,0,],[0,0,],[0,0]
valor = 0 
NumNegativos = 0

for l in range(2):
    for c in range(3):
        valor[l][c] = int(input("Digite o valor recebido: "))
        if valores[l][c] > 0:
            valor = valor + valores[l][c]
        else :
            NumNegativos += 1
print(valor)
print(NumNegativos)
