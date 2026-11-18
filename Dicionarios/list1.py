aluno1 = {"nome": "Lucas", "media": 7.5} # Criando um dicionario

# Mostrando um valor
print(aluno1["nome"])

# Alterando um valor
aluno1["media"] = 10

# adicionando um valor
aluno1["curso"] = "ADS"

# Excluindo
del aluno1["curso"]

# Mostrando todos os valores
print(aluno1)

# Criando um dicionario contendo vários dicionário dentro
alunos = {
    1: {"nome":"Lucas", "Média": 7.5},
    2: {"nome": "Guilherme", "Média": 10},
    3: {"nome": "João", "Média": 4}
}

# Consultando um valor especifico
print(alunos[1]["nome"])

# alterando
alunos[2]["nome"] = "Zeze diCarmago"

# Adicionando
alunos[4] = {"Nome":"Julia", "Média":"9"}

# Excluindo
del alunos[3]

# Lista de dicionarios
listaAlunos = [
    {"Nome": "Kleber", "Média": 6},
    {"Nome": "Machado", "Média": 7.5},
    {"Nome": "Clarice", "Média": 9}
]
# Mostrando um valor especifico
print(listaAlunos[1]["Nome"])