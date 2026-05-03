import mysql.connector
import bcrypt
from time import sleep

def conexao_sql():
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Senai0602@',
        database = 'SISTEMA_v1'
    )

    cursor = conexao.cursor()
    return conexao, cursor

def menu():

    print('1 - Criar conta')
    print('2 - Login')
    print('3 - Alterar senha')

    opcao = int(input('Digite qual a opção desejada:'))
    return opcao

def criar_conta():
    conexao, cursor = conexao_sql()

    nickname = input('Digite seu nickname:')
    login = input('Digite qual será seu login:')
    senha = input('Digite sua senha:').encode()
    senha_cript = bcrypt.hashpw(senha, bcrypt.gensalt(10))

    sql = """INSERT INTO usuarios (nickname, login, senha)
    VALUES (%s, %s, %s)"""
    dados = (nickname, login, senha_cript)

    print('Processando...')
    sleep(2)

    cursor.execute(sql, dados)
    conexao.commit()
    print('Conta criada!!')

    cursor.close()
    conexao.close()

def main():
    opcao = menu()
    if opcao == 1:
        criar_conta()

main()