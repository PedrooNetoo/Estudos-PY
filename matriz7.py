nomesProdutos = [['','',''],['','',''],['','','']]
for l in range (3):
    for c in range (3):
        nomesProdutos[l][c] = input("Digite o nome do produto: ")

linha = int(input("Digite a linha desejada: "))
coluna = int(input("Digite a coluna desejada: "))
print(nomesProdutos)