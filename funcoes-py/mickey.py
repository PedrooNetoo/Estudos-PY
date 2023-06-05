nome = input("Digite seu nome: ").lower()

if ("mickey" in nome):
    if("deep web" in nome):
        res="sim"
    else:
        res=input("Da deep web? ").lower()
    if(res == "sim"):
        print("Bem-vindo Mickey Da Deep Web!")
    else:
        print("FODA-SE")
else:
    print(f"Quem é {nome}?")