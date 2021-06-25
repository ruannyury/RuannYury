from flask import Flask, request, url_for, redirect, render_template, flash
from app.models.tables import Cliente


app = Flask(__name__)
app.config.from_object('config')

idGeralCliente = 4
codigoGeralCliente = 400


def refresh1(cliente):
    global idGeralCliente
    global codigoGeralCliente
    idGeralCliente += 1
    codigoGeralCliente += 100
    clientes.append(cliente)


def deletar(cliente):
    clientes.remove(cliente)


# Instanciar os Clientes
clientes = [Cliente(1, "Ruann Yury", 100, '200.100.345-34', 'fisica'),
            Cliente(2, "Israelzin", 200, '200.100.346-34', 'fisica'),
            Cliente(3, "Rafolas", 300, '200.100.347-34', 'juridica')]


@app.route("/PaginaInicial")
@app.route("/home")
@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/create", methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        if request.form['fisijurid'] == '1':
            cliente = Cliente(idGeralCliente, request.form['nome'], codigoGeralCliente, request.form['cpfcnpj'], 'P. Física')
            refresh1(cliente)
            flash('Adicionado!')
            return redirect(url_for('visualizar'))
        elif request.form['fisijurid'] == '2':
            cliente = Cliente(idGeralCliente, request.form['nome'], codigoGeralCliente, request.form['cpfcnpj'], 'P. Jurídica')
            refresh1(cliente)
            flash('Adicionado!')
            return redirect(url_for('visualizar'))
        else:
            flash('Escolha direito!')
            return redirect(url_for('adicionar'))
    return render_template('create.html')


@app.route("/read")
def visualizar():
    return render_template('visualizar.html', clientes=clientes)


@app.route("/update", methods=['GET', 'POST'])
def atualizar():
    if request.method == 'POST':
        cliente_id = int(request.form['id'])
        cliente = [c for c in clientes if cliente_id == c.get_id()][0]
        cliente.set_nome(request.form['nome'])
        cliente.set_cnpjcpf(request.form['cpfcnpj'])
        flash('Atualizado com sucesso!')
        return redirect(url_for('visualizar'))
    return render_template('atualizar.html')


@app.route("/delete", methods=['GET', 'POST'])
def remover():
    if request.method == 'POST':
        cliente_id = int(request.form['id'])
        cliente = [c for c in clientes if cliente_id == c.get_id()][0]
        deletar(cliente)
        flash('Removido com sucesso, seu bosta!')
        return redirect(url_for('visualizar'))
    else:
        return render_template('remover.html')
