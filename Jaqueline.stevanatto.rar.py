# -*- coding: utf-8 -*-
"""Cópia de Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gwxJxCIRHos_q7bqC1HYrTKalFka8OOd
"""

opcao = ""
escolha = ""
lista = list()
while True:

    menu = print("""Menu Principal
    n1. Estudante
    n2. Disciplina
    n3. Professor
    n4. Turma
    n5. Matrícula
    n6. Disciplina""")
    opcao = str(input("digite a alternativa desejada: "))
    print("você digitou a opção {}\n\n".format(opcao))

    if opcao == "1":
        print("""Estudante
        n1. Incluir 
        n2. listar 
        n3. atualizar 
        n4. Excluir 
        n5. Sair
        """)
        escolha = input("digite a alternativa desejada :")
        print('Você digitou a opção: {}\n\n'.format(opcao))
        
        if escolha == "1":
          print("Incluir \n\n")
          nome = str(input("Nome Completo: "))

          if nome not in lista:
            lista.append(nome)
            print("nome cadastrado com sucesso!\n\n")

          else:
            print("nome já cadastrado\n\n")

        elif escolha == "2":
          print("Listar \n\n")
          for nome in (lista):
                print(nome)

        elif escolha == "3":
          print("Alterar \n\n")
          nome = str(input("Nome Completo: "))
          for nome in lista:
                lista.index(nome)
          nome = str(input("Nome Completo: "))
          print("nome alterado com sucesso!\n\n")

        elif escolha == "4":
          print("Excluir \n\n")
          nome = str(input("Nome Completo: "))
          for nome in lista:
                lista.remove(nome)


        elif escolha == "5":
          print("Saindo \n\n")
          break

        else:
          ('Opção não encontrada \n\n' )

    elif opcao == "2":
        print("Disciplina \n\n")

    elif opcao == "3":
        print("Professores \n\n")

    elif opcao == "4":
        print("Turmas \n\n")

    elif opcao == "5":
        print("Matriculas \n\n")

    elif opcao == "6":
        print("Saindo \n\n")
        break

    else:
      print ('Opção não encontrada \n\n' )



