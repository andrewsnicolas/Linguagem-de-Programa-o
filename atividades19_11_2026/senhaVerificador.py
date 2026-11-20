def verificar_senha(senha)
    tem_8_caracte = len(senha) == 8
    tem_maiusculo = senha != senha.lower()
    tem_minusculo = senha != senha.upper()
    tem_al_numero = any(char.isdigit() for char in senha)
    tem_carac_esp = senha.isalnum()
    
    if(not tem_8_caracte):
        print("A senha digitada não tem 8 caracteres")
    if(not tem_maiusculo):
        print("A sua senha não tem letras maiúsculas")
    if(not tem_minusculo):
        print("A sua senha não tem letras minúsculas")
    if(not tem_al_numero):
        print("A sua senha não tem números")
    if(not tem_carac_esp):
        print("A sua senha não tem caractere especial")
    
    tudo_certo = tem_8_caracte and tem_maiusculo and tem_minusculo and tem_al_numero and tem_carac_esp
    return tudo_certo


tudo_certo = False
while(not tudo_certo):
    senha = input("Digite a senha: ")
    tudo_certo = verificar_senha(tudo_certo)
    if(tudo_certo):
        print("A sua senha foi aceita!")
    else:
        print("A sua senha não foi aceita.")


