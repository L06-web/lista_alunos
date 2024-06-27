def menu():
    print("\n----- Menu -----")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Remover aluno")
    print("4 - Procurar aluno")
    print("5 - Listar aprovados")
    print("6 - Listar reprovados")
    print("7 - Procurar pelo nome do aluno")
    print("8 - Média da turma B1")
    print("9 - Média da turma B2")
    print("10 - Média da turma geral")
    print("11 - Diário da turma geral")
    print("0 - Sair")
    return input("Escolha uma opção: ")

alunos = []

def adicionar():
    while True:
        nome = input("Informe seu nomee: ")
        if len(nome) <= 27:
            nome = nome.ljust(27)
            break
        else:
            print("O nome deve ter no máximo 27 caracteres. Tente novamente.")
    while True:
        ra = input("Informe o RA do aluno: ")
        if len(ra) <= 5:
            ra = ra.zfill(5)
            break
        else:
            print("O RA deve ter no máximo 5 caracteres. Tente novamente.")
    while True:
        try:
            nota_b1 = float(input("Informe a nota B1: "))
            if 0 <= nota_b1 <= 10:
                break
            else:
                print("A nota B1 deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Nota B1 inválida. Digite um número entre 0 e 10.")
    while True:
        try:
            nota_b2 = float(input("Informe a Nota B2: "))
            if 0 <= nota_b2 <= 10:
                break
            else:
                print("A Nota B2 deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Nota B2 inválida. Digite um número entre 0 e 10.")
    aluno = {
        "RA": ra,
        "Nome": nome,
        "Nota B1": nota_b1,
        "Nota B2": nota_b2
    }
    alunos.append(aluno)
    print("Aluno adicionado com sucesso!")
    print(aluno)
    return aluno

def listar():
    print("\n----- Lista de Alunos -----")
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f'RA: {aluno["RA"]} - Nome: {aluno["Nome"]} - Nota B1: {aluno["Nota B1"]} - Nota B2: {aluno["Nota B2"]}')
    input('Aperte qualquer tecla para continuar')

def remover():
    ra = input('Digite o RA do aluno: ')
    for aluno in alunos:
        if aluno["RA"] == ra:
            alunos.remove(aluno)
            print(f'Aluno com RA {ra} removido com sucesso!')
            break
    else:
        print(f'Aluno com RA {ra} não encontrado.')
    input('Aperte qualquer tecla para continuar')

def procurar():
    ra = input('Digite o RA do aluno que deseja procurar: ')
    for aluno in alunos:
        if aluno["RA"] == ra:
            print(f'Aluno encontrado: RA: {aluno["RA"]}, Nome: {aluno["Nome"].strip()}, Nota B1: {aluno["Nota B1"]}, Nota B2: {aluno["Nota B2"]}')
            break
    else:
        print(f'Aluno com RA {ra} não encontrado.')
    input('Aperte qualquer tecla para continuar')

def aprovados():
    print("\n----- Lista de Alunos Aprovados -----")
    aprovados = [aluno for aluno in alunos if (aluno["Nota B1"] + aluno["Nota B2"]) / 2 >= 7.0]
    if not aprovados:
        print("Nenhum aluno aprovado.")
    else:
        for aluno in aprovados:
            print(f'RA: {aluno["RA"]} - Nome: {aluno["Nome"].strip()} - Nota B1: {aluno["Nota B1"]} - Nota B2: {aluno["Nota B2"]} - Média: {(aluno["Nota B1"] + aluno["Nota B2"]) / 2}')
    input('Aperte qualquer tecla para continuar')

def reprovados():
    print("\n----- Lista de Alunos Reprovados -----")
    reprovados = [aluno for aluno in alunos if (aluno["Nota B1"] + aluno["Nota B2"]) / 2 < 7.0]
    if not reprovados:
        print("Nenhum aluno reprovado.")
    else:
        for aluno in reprovados:
            print(f'RA: {aluno["RA"]} - Nome: {aluno["Nome"].strip()} - Nota B1: {aluno["Nota B1"]} - Nota B2: {aluno["Nota B2"]} - Média: {(aluno["Nota B1"] + aluno["Nota B2"]) / 2}')
    input('Aperte qualquer tecla para continuar')

def procuranome():
    nome = input('Digite o nome do aluno que deseja procurar: ').strip().lower()
    encontrados = [aluno for aluno in alunos if nome in aluno["Nome"].strip().lower()]
    if encontrados:
        print("\n----- Alunos Encontrados -----")
        for aluno in encontrados:
            print(f'RA: {aluno["RA"]} - Nome: {aluno["Nome"].strip()} - Nota B1: {aluno["Nota B1"]} - Nota B2: {aluno["Nota B2"]}')
    else:
        print(f'Nenhum aluno com o nome "{nome}" foi encontrado.')
    input('Aperte qualquer tecla para continuar')

def media_b1():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        soma_b1 = sum(aluno["Nota B1"] for aluno in alunos)
        media_b1 = soma_b1 / len(alunos)
        print(f'Média da turma B1: {media_b1:.2f}')
    input('Aperte qualquer tecla para continuar')

def media_b2():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        soma_b2 = sum(aluno["Nota B2"] for aluno in alunos)
        media_b2 = soma_b2 / len(alunos)
        print(f'Média da turma B2: {media_b2:.2f}')
    input('Aperte qualquer tecla para continuar')

def media_geral():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        soma_total = sum(aluno["Nota B1"] + aluno["Nota B2"] for aluno in alunos)
        media_geral = soma_total / (2 * len(alunos))
        print(f'Média geral da turma: {media_geral:.2f}')
    input('Aperte qualquer tecla para continuar')

def diario():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        input('Aperte qualquer tecla para continuar')
        return
    
    print("\n--------------------------------------------------------")
    print("                     Diário da turma                     ")
    print("--------------------------------------------------------")
    print("RA     Nome                        Nota B1   Nota B2   Média")
    print("--------------------------------------------------------")
    
    soma_b1 = soma_b2 = 0
    
    for aluno in alunos:
        ra = aluno["RA"]
        nome = aluno["Nome"].strip()
        nota_b1 = aluno["Nota B1"]
        nota_b2 = aluno["Nota B2"]
        media = (nota_b1 + nota_b2) / 2
        soma_b1 += nota_b1
        soma_b2 += nota_b2
        print(f'{ra.ljust(5, " ")}  {nome.ljust(27, " ")}  {str(nota_b1).rjust(6, " ")}  {str(nota_b2).rjust(6, " ")}  {str(media).rjust(6, " ")}')
    
    media_b1_turma = soma_b1 / len(alunos)
    media_b2_turma = soma_b2 / len(alunos)
    media_geral_turma = (soma_b1 + soma_b2) / (2 * len(alunos))
    
    print("--------------------------------------------------------")
    print(f'Médias da Turma                     {str(media_b1_turma).rjust(6, " ")}  {str(media_b2_turma).rjust(6, " ")}  {str(media_geral_turma).rjust(6, " ")}')
    print("--------------------------------------------------------")
    
    input('Aperte qualquer tecla para continuar')


if __name__ == '__main__':
    while True:
        match menu():
            case '1':
                adicionar()
            case '2':
                listar()
            case '3':
                remover()
            case '4':
                procurar()
            case '5':
                aprovados()
            case '6':
                reprovados()
            case '7':
                procuranome()
            case '8':
                media_b1()
            case '9':
                media_b2()
            case '10':
                media_geral()
            case '11':
                diario()
            case '0':
                break       
