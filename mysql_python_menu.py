import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="escola"
)

cursor = conexao.cursor()

while True:

    print("\n1 - Cadastrar")
    print("2 - Buscar Nome")
    print("3 - Mostrar Todos")
    print("4 - Sair")

    opcao = input("Escolha: ")

    # CADASTRAR
    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        curso = input("Curso: ")

        sql = "INSERT INTO alunos (nome, idade, curso) VALUES (%s,%s,%s)"
        dados = (nome, idade, curso)

        cursor.execute(sql, dados)
        conexao.commit()

        print("Pessoa cadastrada com sucesso!")

    # BUSCAR
    elif opcao == "2":
        nome = input("Digite o nome para buscar: ")

        sql = "SELECT * FROM alunos WHERE nome = %s"
        cursor.execute(sql, (nome,))

        resultado = cursor.fetchall()

        # Se não encontrar ninguém
        if len(resultado) == 0:
            print("Usuário não localizado!")

        else:
            for pessoa in resultado:
                print(pessoa)

    # MOSTRAR TODOS
    elif opcao == "3":

        cursor.execute("SELECT * FROM alunos")

        resultado = cursor.fetchall()

        for pessoa in resultado:
            print(pessoa)

    elif opcao == "4":
        break

cursor.close()
conexao.close()