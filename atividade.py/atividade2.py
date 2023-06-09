def calcularMedia (nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if(media >= 7):
        print("Aprovado")
    else:
        print("Reprovado")

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

calcularMedia(nota1, nota2, nota3)