def isSozinhoNoSetor(qtd):
    if(qtd == 1):
        return "Sozinho no setor."
    else:
        return "Não está sozinho no setor"

def soma(x,y):  
    return x+y

def aoQuadrado(z):
    return z*z

def calcularPerimetro(larg, comprimento):
    return (2*larg) + (2*comprimento)

def getMedia(x, y, z):
    media = (x+y+z) / 3
    if(media >= 7):
        return "Aprovado"
    else:
        return "Reprovado"
    
def verificarVogais(lista):
    vogais = ["a", "e", "i", "o", "u"]
    for letra in lista:
        if(letra in vogais): 
            print(letra)
    return True
