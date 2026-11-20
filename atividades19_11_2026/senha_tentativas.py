#Variáveis
senha_acesso = "Abacate"

acesso_liberado = False

senha_digitada = " "


for cont in range(1, 4):
    senha_digitada = input(f"Digite a senha ({cont}° tentativa): ")
    if(senha_digitada == senha_acesso): 
        print("Senha correta!")
        acesso_liberado = True
        break
    else: print("Senha incorreta!")
    

if(acesso_liberado): print("Acesso Liberado!")
else: print("Acesso negado!")