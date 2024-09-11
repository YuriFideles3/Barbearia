import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin123',
            database='barbearia'
        )
        if conexao.is_connected():
            print('Conexão ao banco de dados MySQL estabelecida com sucesso!')
            return conexao
    except mysql.connector.Error as erro:
        print(f'Erro ao conectar ao banco de dados MySQL: {erro}')

def desconectar(conexao):
    if conexao.is_connected():
        conexao.close()
        print('Conexão ao banco de dados MySQL encerrada.')
