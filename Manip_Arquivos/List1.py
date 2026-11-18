import json

# Abrindo um arquivo
arquivoSisNotas = open("alunos.json", "w", encoding="utf-8") # "nome-do-arquivo", "modo de abertura do arquivo", "Codificação"

##
# w - write - cria arquivo caso não exista
# r - read - consulta os arquivos
# a - append - acrescenta dados
##

# Recuperandoo arquivos json
arquivoSisNotas = open("alunos.json", "r", encoding="utf-8")
alunos = json.load(arquivoSisNotas)
arquivoSisNotas.close()

# Manipulando os dados recuperados
print(alunos["2"]["media"])

# Armazenando uma estrutura de dados compativel com o JSON
alunos = {
    1: {"nome": "Cleber", "media": 7.5},
    2: {"nome": "Maria", "media": 9.5},
    3: {"nome": "Sandro", "media": 7.5}
}

arquivoSisNotas = open("alunos.json", "w", encoding="utf-8")
json.dump(alunos, arquivoSisNotas, ensure_ascii=False, indent=4)
arquivoSisNotas.close()

# Armazenando os dados em um arquivo-texto (Não JSON)
arquivoTeste = open("teste.txt", "w", encoding="utf-8")
arquivoTeste.write("Teste de gravação de arquivo-texto convencional.")
arquivoTeste.close()

# Fechando o arquivo
arquivoSisNotas.close()

# Fechamento automatico
alunos = {
    1: {"nome": "Cleber", "media": 7.5},
    2: {"nome": "Maria", "media": 9.5},
    3: {"nome": "Sandro", "media": 7.5}
}

with open("alunos.json", "w", encoding="utf-8") as arquivoSisNotas:
    json.dump(alunos, arquivoSisNotas, ensure_ascii=False, indent=4)