matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(3):
    for c in range(3):
      matriz[l][c] = int(input("Digite um numero: "))
      if(l == c):
            matriz[l][c] = matriz[l][c] *5
print(matriz)
