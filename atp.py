import json

# Jaqueline Stevanatto Aluizio


estudante = "estudante.json"
professor = "professor.json"
materia = "materia.json"
turma = "turma.json"
matricula = "matricula.json"
lista_x = "pasta"
mat = "matricula"


def cabecalho(txt):
    print("{:^30}".format(txt))

def menu():
    cabecalho("Menu")
    print("""
    [1] Estudante
    [2] Professor
    [3] Disciplina
    [4] Turma
    [5] Matricula
    [6] Sair""")
    return str(input("Escolha uma das opções: "))


def menu_inicial():
    print("""
    [1] Cadastrar
    [2] Listar
    [3] Alterar
    [4] Excluir
    [5] Sair""")
    return str(input("Digite a opcao desejada: "))


def inserir(arquivo):
    nome = str(input("Digite o nome : "))
    cpf = str(input("Digite o CPF: "))
    mat = int(input("Digite a matricula: "))
    pessoa = {
        "nome": nome,
        "cpf": cpf,
        "mat": mat,
    }
    lista_x = ler_arquivo(arquivo)
    if pessoa in lista_x:
        print("este cadastro já foi realizado")
    else:
        lista_x.append(pessoa)
    salvar_arquivos(lista_x, arquivo)
    return


def alterar_matricula(arquivo):
    lista_x = ler_arquivo("arquivo")
    mat = input('Digite a matricula que deseja excluir: ')
    for materia in lista_x:
        if materia[mat] == mat:
            materia["nome"] = input("digite o novo nome: ")
            salvar_arquivos(lista_x, arquivo)
            return
    print("Esse cadastro não foi encontrado")


def alterar(arquivo):
    lista_x = ler_arquivo(arquivo)
    for pessoa in lista_x:
        if pessoa[mat] == mat:
            pessoa["nome"] = input("digite o novo nome: ")
            pessoa["cpf"] = input("digite o novo cpf: ")
            salvar_arquivos(lista_x, arquivo)
            return
    print("Esse cadastro não foi encontrado")


def listar(arquivo):
    lista_x = ler_arquivo(arquivo)
    if len(lista_x) == 0:
        print("não há nenhum cadastro")
    else:
        for x in lista_x:
            print("nome:", x["nome"], "cpf:", x["cpf"], "mat:", x["mat"])


def excluir(arquivo):
    mat = input('Digite a matricula que deseja excluir: ')

    dado_removido = None
    for dados_x in lista_x:
        if dados_x[mat] == mat:
            dado_removido = dados_x
            break

    if dado_removido is not None:
        lista_x.remove(dado_removido)
        salvar_arquivos(lista_x, arquivo)


def salvar_arquivos(lista_x, arquivo_x):
    with open(arquivo_x, "w", encoding= 'utf-8') as abrir_arquivo:
        json.dump(lista_x, abrir_arquivo, ensure_ascii=False)


def ler_arquivo(arquivo_x):
    try:
        with open(arquivo_x, "r", encoding= 'utf-8') as abrir_arquivo:
            lista_x = json.load(abrir_arquivo, ensure_ascii=False)

        return lista_x
    except:
        return []


def sistema_secundario(arquivo):
    while True:
        op_gerais = menu_inicial()
        if op_gerais == '1':
            cabecalho("Cadastrar")
            inserir(arquivo)
        elif op_gerais == '2':
            cabecalho("Listar")
            listar(arquivo)
        elif op_gerais == '3':
            cabecalho("Alterar")
            alterar(arquivo)
        elif op_gerais == '4':
            cabecalho("Excluir")
            excluir(arquivo)
        elif op_gerais == '5':
            cabecalho("Sair ")
            break
        else:
            print("ERRO")


while True:
    op = menu()
    if op == '1':
        sistema_secundario(estudante)
    elif op == '2':
        sistema_secundario(professor)
    elif op == '3':
        sistema_secundario(materia)
    elif op == '4':
        sistema_secundario(turma)
    elif op == '5':
        sistema_secundario(matricula)
    elif op == "6":
        print("Sair")
        break
    else:
        print("ERRO")