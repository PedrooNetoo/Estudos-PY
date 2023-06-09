def calcularTotal(preco, quantidade):
    resultado = preco*quantidade
    print(resultado)
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade que foi adquirida: "))
calcularTotal(preco,quantidade)