from funcoes import isSozinhoNoSetor
    
qtdSetores = int(input("Digite a quantidade de setores: "))
for x in range(qtdSetores):
    setor = x+1
    pessoas = int(input(f"Digite a quantidade de pessoas no setor {setor}: "))
    print(isSozinhoNoSetor(pessoas))
    