def converte (hora, minuto , segundo):
    resultado = (hora*3600) + (minuto*60) + (segundo)
    print(resultado)



hora = int(input("Digite a hora: "))
minuto = int(input("Digite o minuto: "))
segundo = int(input("Digite o segundo: "))
converte(hora, minuto , segundo)
