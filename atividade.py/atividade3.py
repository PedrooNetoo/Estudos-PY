def calcularVelocidadeMedia (kmInicial , KmFinal , horaInicial, horaFinal):
    velocidadeMedia = (KmFinal-kmInicial) / (horaFinal-horaInicial)
    print(velocidadeMedia)

calcularVelocidadeMedia(10,15,25,40)

kmInicial = int(input("Digite o km inicial: "))
KmFinal = int(input("Digite o km final: "))
horaInicial = int(input("Digite a hora inicial: "))
horaFinal = int(input("Digite a hora final: "))