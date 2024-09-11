from flask import Flask, render_template, redirect, url_for, request
from utils.database import conectar

app = Flask(__name__)

conn = conectar()
cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro_cliente', methods=['GET', 'POST'])
def cadastro_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        contato = request.form['contato']
        cursor.execute('INSERT INTO barbearia.clientes (id_cliente, nome, contato) VALUES (NULL, %s, %s)', (nome, contato))
        conn.commit()
        return redirect(url_for('index'))
    return render_template('cadastro_cliente.html')



@app.route('/agendamento', methods=['GET', 'POST'])
def agendamento():
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        horario = request.form['horario']
        cursor.execute('INSERT INTO barbearia.agendamentos (id_agendamentos, id_cliente, horario) VALUES (NULL, %s, %s)', (cliente_id, horario))
        conn.commit()
        return redirect(url_for('index'))
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    return render_template('agendamento.html', clientes=clientes)

@app.route('/estoque', methods=['GET', 'POST'])
def estoque():
    if request.method == 'POST':
        if 'cadastro_produto' in request.form:
            nome_produto = request.form['nome_produto']
            quantidade = request.form['quantidade']
            cursor.execute('INSERT INTO barbearia.estoque (id_produto, nome_produto, quantidade) VALUES (NULL, %s, %s)', (nome_produto, quantidade))
            conn.commit()
        elif 'atualizar_quantidade' in request.form:
            id_produto = request.form['id_produto']
            nova_quantidade = request.form['nova_quantidade']
            cursor.execute('UPDATE barbearia.estoque SET quantidade = %s WHERE id_produto = %s', (nova_quantidade, id_produto))
            conn.commit()
        return redirect(url_for('estoque'))
    cursor.execute('SELECT * FROM barbearia.estoque')
    produtos = cursor.fetchall()
    return render_template('estoque.html', produtos=produtos)

@app.route('/servico', methods=['GET', 'POST'])
def servico():
    if request.method == 'POST':
        if 'cadastro_servico' in request.form:
            nome_servico = request.form['nome_servico']
            preco = request.form['preco']
            duracao = request.form['duracao']
            cursor.execute('INSERT INTO barbearia.servico (id_servico, nome, preco, duracao, data_criacao, data_atualizacao) VALUES (NULL, %s, %s, %s, NOW(), NOW())', (nome_servico, preco, duracao))
            conn.commit()
        elif 'atualizar_servico' in request.form:
            id_servico = request.form['id_servico']
            nome_servico = request.form['nome_servico']
            preco = request.form['preco']
            duracao = request.form['duracao']
            cursor.execute('UPDATE barbearia.servico SET nome = %s, preco = %s, duracao = %s, data_atualizacao = NOW() WHERE id_servico = %s', (nome_servico, preco, duracao, id_servico))
            conn.commit()
        return redirect(url_for('servico'))
    
    cursor.execute('SELECT * FROM barbearia.servico')
    servico = cursor.fetchall()
    return render_template('servico.html', servicos=servico)



if __name__ == '__main__':
    app.run(debug=True)
