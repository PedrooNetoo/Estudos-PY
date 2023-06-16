cidades = ["","",""]
valores = [[0,0],[0,0],[0,0]]
for cidade in range(3):
    cidades[cidade] = input("Digite o nome da cidade escolhida: ")
    
    for valor in range(2):
        valores[cidade][valor] = float(input("Digite o valor da pitu e da 51 respectivamente: "))

def receberValor(cidades, valores):
    cidadeNome = input("Digite o nome da cidade para saber a bebida: ")
    bebidaNome = input ("Digite o nome da bebida: ")
    for city in range(3):
        if (cidades[city] == cidadeNome.lower()):
            if(bebidaNome.lower() == "pitu"):
                print(f"O valor da pitu em {cidades[city]} é {valores[city]}")
            if(bebidaNome.lower() == "51"):
                print(f"O valor da pitu em {cidades[city]} é {valores[city]}")
            else:
                print("Essa bebida não foi definida.")
            return
        print("Cidade não encontrada.")


receberValor(cidades, valores)


