from flask import Flask, Response, request
import json
from models.models import Cliente, Produto, ItemNotaFiscal, NotaFiscal


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

cliente_list = [
    Cliente(1, 'Ruann', 100, '1234567890', 'P. Física'),
    Cliente(2, 'Yury', 200, '1234567891', 'P. Jurídica')
]

produto_list = [
    Produto(1, 10, 'Arroz', 5.50),
    Produto(2, 20, 'Feijão', 7.00),
    Produto(3, 30, 'Macarrão', 4.00)
]

item_list = [
    ItemNotaFiscal(1, 1, 5, produto_list[0].to_json()),
    ItemNotaFiscal(2, 2, 5, produto_list[1].to_json()),
    ItemNotaFiscal(3, 3, 10, produto_list[2].to_json())
]

nota_list = [
    NotaFiscal(1, 1, cliente_list[0].to_json()),
    NotaFiscal(2, 2, cliente_list[1].to_json())
]

nota_list[0].adicionar_item(item_list[0].to_json())
nota_list[0].adicionar_item(item_list[1].to_json())
nota_list[0].calcular_total_nota()
nota_list[1].adicionar_item(item_list[2].to_json())
nota_list[1].calcular_total_nota()


# Selecionar Tudo
@app.route("/clientes", methods=["GET"])
def seleciona_clientes():
    # usuarios_objetos = Usuario.query.all()
    clientes_json = [cliente.to_json() for cliente in cliente_list]

    return gera_response(200, "clientes", clientes_json)


# Selecionar Individual
@app.route("/cliente/<id>", methods=["GET"])
def seleciona_cliente(id):
    # usuario_objeto = Usuario.query.filter_by(id=id).first()
    # cliente_objeto = None
    for cliente in cliente_list:
        if str(cliente.id) == str(id):
            cliente_objeto = cliente
            cliente_json = cliente_objeto.to_json()

            return gera_response(200, "cliente", cliente_json)


# Cadastrar
@app.route("/cliente", methods=["POST"])
def cria_cliente():
    body = request.get_json()

    try:
        cliente = Cliente(id=body["id"], nome=body["nome"],
                          codigo=body["codigo"], cnpjcpf=body["cnpjcpf"],
                          tipo=body["tipo"])
        cliente_list.append(cliente)
        # db.session.add(usuario)
        # db.session.commit()
        return gera_response(201, "cliente", cliente.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "cliente", {}, "Erro ao cadastrar")


# Atualizar
@app.route("/cliente/<id>", methods=["PUT"])
def atualiza_cliente(id):
    cliente_objeto = None
    for cliente in cliente_list:
        if str(id) == str(cliente.id):
            cliente_objeto = cliente
    body = request.get_json()

    try:
        if 'id' in body:
            cliente_objeto.id = body['id']
        if 'nome' in body:
            cliente_objeto.nome = body['nome']
        if 'codigo' in body:
            cliente_objeto.codigo = body['codigo']
        if 'cnpjcpf' in body:
            cliente_objeto.cnpjcpf = body['cnpjcpf']
        if 'tipo' in body:
            cliente_objeto.tipo = body['tipo']

        cliente_list.append(cliente_objeto)
        return gera_response(200, "cliente", cliente_objeto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "cliente", {}, "Erro ao atualizar")


# Deletar
@app.route("/cliente/<id>", methods=["DELETE"])
def deleta_cliente(id):
    try:
        cliente_objeto = None
        for cliente in cliente_list:
            if str(id) == str(cliente.id):
                cliente_objeto = cliente

        for posicao_cliente in range(0, len(cliente_list)):
            if cliente_list[posicao_cliente] == cliente_objeto:
                del(cliente_list[posicao_cliente])

        return gera_response(200, "cliente", cliente_objeto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "cliente", {}, "Erro ao deletar")


# Selecionar Tudo
@app.route("/produtos", methods=["GET"])
def seleciona_produtos():
    # usuarios_objetos = Usuario.query.all()
    produtos_json = [produto.to_json() for produto in produto_list]

    return gera_response(200, "produtos", produtos_json)


# Selecionar Individual
@app.route("/produto/<id>", methods=["GET"])
def seleciona_produto(id):
    # usuario_objeto = Usuario.query.filter_by(id=id).first()
    produto_objeto = None
    for produto in produto_list:
        if str(id) == str(produto.id):
            produto_objeto = produto
    produto_json = produto_objeto.to_json()

    return gera_response(200, "produto", produto_json)


# Cadastrar
@app.route("/produto", methods=["POST"])
def cria_produto():
    body = request.get_json()

    try:
        produto = Produto(id=body["id"],
                          codigo=body["codigo"],
                          descricao=body["descricao"],
                          valorUnitario=body["valorUnitario"])
        produto_list.append(produto)
        # db.session.add(usuario)
        # db.session.commit()
        return gera_response(201, "produto", produto.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "produto", {}, "Erro ao cadastrar")


# Atualizar
@app.route("/produto/<id>", methods=["PUT"])
def atualiza_produto(id):
    produto_objeto = None
    for produto in produto_list:
        if str(id) == str(produto.id):
            produto_objeto = produto
    body = request.get_json()

    try:
        if 'id' in body:
            produto_objeto.id = body['id']
        if 'codigo' in body:
            produto_objeto.codigo = body['codigo']
        if 'descricao' in body:
            produto_objeto.descricao = body['descricao']
        if 'valorUnitario' in body:
            produto_objeto.valorUnitario = body['valorUnitario']

        produto_list.append(produto_objeto)
        return gera_response(200, "produto", produto_objeto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "produto", {}, "Erro ao atualizar")


# Deletar
@app.route("/produto/<id>", methods=["DELETE"])
def deleta_produto(id):
    try:
        produto_objeto = None
        for produto in produto_list:
            if str(id) == str(produto.id):
                produto_objeto = produto

        for posicao_produto in range(0, len(produto_list)):
            if produto_list[posicao_produto] == produto_objeto:
                del(produto_list[posicao_produto])

        return gera_response(200, "produto", produto_objeto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "produto", {}, "Erro ao deletar")


# Selecionar Tudo
@app.route("/itens", methods=["GET"])
def seleciona_itens():
    # usuarios_objetos = Usuario.query.all()
    itens_json = [item.to_json() for item in item_list]

    return gera_response(200, "itens", itens_json)


# Selecionar Individual
@app.route("/item/<id>", methods=["GET"])
def seleciona_item(id):
    # usuario_objeto = Usuario.query.filter_by(id=id).first()
    item_objeto = None
    for item in item_list:
        if str(id) == str(item.id):
            item_objeto = item
    item_json = item_objeto.to_json()

    return gera_response(200, "item", item_json)


# Cadastrar
@app.route("/item", methods=["POST"])
def cria_item():
    body = request.get_json()

    try:
        item = ItemNotaFiscal(id=body["id"],
                              sequencial=body["sequencial"],
                              quantidade=body["quantidade"],
                              produto=body["produto"])
        item_list.append(item)
        # db.session.add(usuario)
        # db.session.commit()
        return gera_response(201, "item", item.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "item", {}, "Erro ao cadastrar")


# Atualizar
@app.route("/item/<id>", methods=["PUT"])
def atualiza_item(id):
    item_objeto = None
    for item in item_list:
        if str(id) == str(item.id):
            item_objeto = item
    body = request.get_json()

    try:
        if 'id' in body:
            item_objeto.id = body['id']
        if 'sequencial' in body:
            item_objeto.sequencial = body['sequencial']
        if 'quantidade' in body:
            item_objeto.quantidade = body['quantidade']
        if 'produto' in body:
            item_objeto.produto = body['produto']

        item_list.append(item_objeto)
        return gera_response(200, "item", item_objeto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "item", {}, "Erro ao atualizar")


# Deletar
@app.route("/item/<id>", methods=["DELETE"])
def deleta_item(id):
    try:
        item_objeto = None
        for item in item_list:
            if str(id) == str(item.id):
                item_objeto = item

        for posicao_item in range(0, len(item_list)):
            if item_list[posicao_item] == item_objeto:
                del(item_list[posicao_item])

        return gera_response(200, "item", item_objeto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "item", {}, "Erro ao deletar")


# Selecionar Tudo
@app.route("/notas", methods=["GET"])
def seleciona_notas():
    # usuarios_objetos = Usuario.query.all()
    notas_json = [nota.to_json() for nota in nota_list]

    return gera_response(200, "notas", notas_json)


# Selecionar Individual
@app.route("/nota/<id>", methods=["GET"])
def seleciona_nota(id):
    # usuario_objeto = Usuario.query.filter_by(id=id).first()
    nota_objeto = None
    for nota in nota_list:
        if str(id) == str(nota.id):
            nota_objeto = nota
    nota_json = nota_objeto.to_json()

    return gera_response(200, "nota", nota_json)


# Cadastrar
@app.route("/nota", methods=["POST"])
def cria_nota():
    body = request.get_json()

    try:
        nota = NotaFiscal(id=body["id"],
                          codigo=body["codigo"],
                          cliente=body["cliente"],
                          lista_itens=body['itens'])

        # nota.str_itens(body['itens'])

        nota_list.append(nota)

        return gera_response(201, "nota", nota.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "nota", {}, "Erro ao cadastrar")


# Atualizar
@app.route("/nota/<id>", methods=["PUT"])
def atualiza_nota(id):
    nota_objeto = None
    for nota in nota_list:
        if str(id) == str(nota.id):
            nota_objeto = nota
    body = request.get_json()

    try:
        if 'id' in body:
            nota_objeto.id = body['id']
        if 'codigo' in body:
            nota_objeto.codigo = body['codigo']
        if 'cliente' in body:
            nota_objeto.cliente = body['cliente']
        if 'itens' in body:
            nota_objeto.lista_itens = body['itens']

        nota_list.append(nota_objeto)
        return gera_response(200, "nota", nota_objeto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "nota", {}, "Erro ao atualizar")


# Deletar
@app.route("/nota/<id>", methods=["DELETE"])
def deleta_nota(id):
    try:
        nota_objeto = None
        for nota in nota_list:
            if str(id) == str(nota.id):
                nota_objeto = nota

        for posicao_nota in range(0, len(nota_list)):
            if nota_list[posicao_nota] == nota_objeto:
                del(nota_list[posicao_nota])

        return gera_response(200, "nota", nota_objeto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "nota", {}, "Erro ao deletar")


# Calcular
@app.route("/calculanf/<id>", methods=["GET"])
def calcula_nota(id):
    try:
        nota_objeto = None
        for nota in nota_list:
            if str(id) == str(nota.id):
                nota_objeto = nota

        total_nota = nota_objeto.calcular_total_nota(True)

        return gera_response(200, "calculanf", f'Total: {total_nota}', "Calculado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "calculanf", {}, "Erro ao calcular")


# Imprime
@app.route("/imprimenf/<id>", methods=["GET"])
def imprime_nota(id):
    try:

        nota_objeto = None
        for nota in nota_list:
            if str(id) == str(nota.id):
                nota_objeto = nota
        nota_objeto.calcular_total_nota()
        nota_impressa = nota_objeto.imprimir_nota_fiscal()

        return gera_response(200, "imprimenf", nota_impressa, "Impressa com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "imprimenf", {}, "Erro ao imprimir")


def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if mensagem:
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")


app.run(debug=True)
