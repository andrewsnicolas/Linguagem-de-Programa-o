def formatar_nome_abnt(nome):
    nome_vetor = nome.split(" ")
    ult_nome = nome_vetor[(len(nome_vetor)-1)]
    pri_nome = nome_vetor[0]
    nome_abnt = ult_nome + ", " + pri_nome[0]
    return nome_abnt

nome = input("Digite o seu nome: ")
nome_formatado = formatar_nome_abnt(nome)
print(f"Seu nome para referências/citações em ABNT: {nome_formatado}")