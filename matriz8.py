senhas = [['',''],['','']]

for l in range(2):
        for c in range(2):
                senhas[l][c] = input("Digite a senha do seu banco: ")

verificacao = input("Digite sua senha: ").lower()  
senha_correta = False

for linha in senhas:
        for coluna in linha:
                if verificacao == coluna:
                        senha_correta = True
                        break
                
if senha_correta:
        print("Usuario Apto!")
else:
        print("Usuario Inexistente")