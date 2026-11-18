import json
from pathlib import Path
from time import sleep

SistemaAlunos = {}  # Dicionario de alunos e notas, tera chave de identificação do dados com RA
sisNotas = Path("alunos.json")

def adicionarAluno():
    ra = int(input("Digite o RA do aluno: "))
    if ra in SistemaAlunos:
        print("RA ja existente!!")
    else:
        nome = input("Nome do aluno: ").capitalize()
        media = float(input("Média do aluno: "))
        SistemaAlunos[ra] = {"Aluno": nome, "Média": media}
        salvarAlunosNoArquivo(SistemaAlunos)
        print("Aluno adicionado ao sistema!")

def atualizarAluno():
    ra = int(input("Digite o RA do aluno que quer atualizar: "))
    if ra in SistemaAlunos:
        print(f"Aluno atual: {SistemaAlunos[ra]["Aluno"]} \nMédia: {SistemaAlunos[ra]["Média"]}")
        nome = input("Novo nome: ")
        media = float(input("Nova média: "))
    
        if nome:
            SistemaAlunos[ra]["Aluno"] = nome
        if media:
            SistemaAlunos[ra]["Média"] = media
        salvarAlunosNoArquivo(SistemaAlunos)
        print("Dados atualizados com successo")
    
    else:
        print("RA não encontrado")

def removerAluno():
    ra = int(input("Digite o RA do aluno que deseja remover: "))
    if ra in SistemaAlunos:
        del SistemaAlunos[ra]
        salvarAlunosNoArquivo(SistemaAlunos)
        print("Aluno removido com sucesso")
    else:
        print("RA não encontrado")

def listarAlunos():
    if not SistemaAlunos:
        print("Nenhum aluno cadastro no sistema.")
    else:
        for ra, dados in SistemaAlunos.items():
            print(f"RA: {ra} | Nome: {dados["Aluno"]} | Média: {dados["Média"]}")

def carregarArquivo():
    if sisNotas.exists():
        with open(sisNotas, "r", encoding="utf-8") as arquivo:
            print("Arquivo carregado com sucesso")
            return json.load(arquivo)
    print("Nenhum arquivo encontrado, gerando um vazio...")
    sleep(2)
    return {}

def salvarAlunosNoArquivo(alunos):
    with open(sisNotas, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, ensure_ascii=False, indent=4)
    print("Mudanças no arquivo salvas!")

def menu():
    SistemaAlunos = carregarArquivo()
    escolha = 0
    while escolha != 5:
        try:
            print("""
            [ 1 ] Adicionar aluno
            [ 2 ] Atualizar aluno
            [ 3 ] Remover aluno
            [ 4 ] Listar alunos
            [ 5 ] Sair
            """)
            escolha = int(input("Escolha uma das alternativas: "))
            while escolha < 0 or escolha > 5:
                escolha = int(input("Digite uma alternativa válida: "))   
        except ValueError:
            print("Erro de valor inserido")
            menu()

        match escolha:
            case 1:
                adicionarAluno()

            case 2:
                atualizarAluno()
                
            case 3:
                removerAluno()
            case 4:
                listarAlunos()
            case 5:
                print("Saindo do sistema de notas...")
                sleep(2)


menu()