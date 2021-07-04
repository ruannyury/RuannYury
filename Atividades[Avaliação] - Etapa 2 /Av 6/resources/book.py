from flask import request
from flask_restplus import Resource, fields

from models.book import BookModel, ClienteModel, ProdutoModel, ItemModel, NotaFiscalModel
from schemas.book import BookSchema, ClienteSchema, ProdutoSchema, ItemSchema, NotaFiscalSchema

from server.instance import server

book_ns = server.book_ns
cliente_ns = server.cliente_ns
produto_ns = server.produto_ns
item_ns = server.item_ns
nota_fiscal_ns = server.nota_fiscal_ns

ITEM_NOT_FOUND = "Item not found."
PRODUTO_NOT_FOUND = "Produto not found."
CLIENTE_NOT_FOUND = "Cliente not found."
NOTA_NOT_FOUND = "Nota Fiscal not found."

book_schema = BookSchema()
cliente_schema = ClienteSchema()
produto_schema = ProdutoSchema()
item_schema = ItemSchema()
nota_fiscal_schema = NotaFiscalSchema()

book_list_schema = BookSchema(many=True)
cliente_list_schema = BookSchema(many=True)
produto_list_schema = BookSchema(many=True)
item_list_schema = BookSchema(many=True)
nota_fiscal_list_schema = BookSchema(many=True)

# Model required by flask_restplus for expect
item1 = book_ns.model('Book', {
    'title': fields.String('Book title'),
    'pages': fields.Integer(0),
})
cliente = cliente_ns.model('Cliente', {
    'nome': fields.String(160),
    'codigo': fields.Integer,
    'cnpjcpf': fields.String(160),
    'tipo': fields.String(160)
})
produto = produto_ns.model('Produto', {
    'descricao': fields.String(160),
    'valor_unidade': fields.Float
})
item = item_ns.model('Item', {
    'sequencial': fields.Integer,
    'quantidade': fields.Integer
})
nota_fiscal = nota_fiscal_ns.model('NotaFiscal', {
    'codigo': fields.Integer,
    'data': fields.Date,
    'valorNota': fields.Float
})


class Book(Resource):

    def get(self, id):
        book_data = BookModel.find_by_id(id)
        if book_data:
            return book_schema.dump(book_data)
        return {'message': ITEM_NOT_FOUND}, 404

    def delete(self, id):
        book_data = BookModel.find_by_id(id)
        if book_data:
            book_data.delete_from_db()
            return '', 204
        return {'message': ITEM_NOT_FOUND}, 404

    @book_ns.expect(item1)
    def put(self, id):
        book_data = BookModel.find_by_id(id)
        book_json = request.get_json()

        if book_data:
            book_data.pages = book_json['pages']
            book_data.title = book_json['title']
        else:
            book_data = book_schema.load(book_json)

        book_data.save_to_db()
        return book_schema.dump(book_data), 200


class BookList(Resource):
    @book_ns.doc('Get all the Items')
    def get(self):
        return book_list_schema.dump(BookModel.find_all()), 200

    @book_ns.expect(item1)
    @book_ns.doc('Create an Item')
    def post(self):
        book_json = request.get_json()
        book_data = book_schema.load(book_json)

        book_data.save_to_db()

        return book_schema.dump(book_data), 201


class Cliente(Resource):

    def get(self, id):
        cliente_data = ClienteModel.find_by_id(id)
        if cliente_data:
            return cliente_schema.dump(cliente_data)
        return {'message': ITEM_NOT_FOUND}, 404

    def delete(self, id):
        cliente_data = ClienteModel.find_by_id(id)
        if cliente_data:
            cliente_data.delete_from_db()
            return '', 204
        return {'message': ITEM_NOT_FOUND}, 404

    @book_ns.expect(cliente)
    def put(self, id):
        cliente_data = ClienteModel.find_by_id(id)
        cliente_json = request.get_json()

        if cliente_data:
            cliente_data.nome = cliente_json['nome']
            cliente_data.codigo = cliente_json['codigo']
            cliente_data.cnpjcpf = cliente_json['cnpjcpf']
            cliente_data.tipo = cliente_json['tipo']
        else:
            cliente_data = cliente_schema.load(cliente_json)

        cliente_data.save_to_db()
        return cliente_schema.dump(cliente_data), 200


class ClienteList(Resource):
    @cliente_ns.doc('Get all the clientes.')
    def get(self):
        return cliente_list_schema.dump(ClienteModel.find_all()), 200

    @cliente_ns.expect(cliente)
    @cliente_ns.doc('Create an cliente')
    def post(self):
        cliente_json = request.get_json()
        cliente_data = cliente_schema.load(cliente_json)

        cliente_data.save_to_db()

        return cliente_schema.dump(cliente_data), 201


class Produto(Resource):

    def get(self, id):
        produto_data = ProdutoModel.find_by_id(id)
        if produto_data:
            return produto_schema.dump(produto_data)
        return {'message': ITEM_NOT_FOUND}, 404

    def delete(self, id):
        produto_data = ProdutoModel.find_by_id(id)
        if produto_data:
            produto_data.delete_from_db()
            return '', 204
        return {'message': ITEM_NOT_FOUND}, 404

    @produto_ns.expect(produto)
    def put(self, id):
        produto_data = ProdutoModel.find_by_id(id)
        produto_json = request.get_json()

        if produto_data:
            produto_data.descricao = produto_json['descricao']
            produto_data.valor_unidade = produto_json['valor_unidade']
        else:
            produto_data = produto_schema.load(produto_json)

        produto_data.save_to_db()
        return produto_schema.dump(produto_data), 200


class ProdutoList(Resource):
    @produto_ns.doc('Get all the produtos.')
    def get(self):
        return produto_list_schema.dump(ProdutoModel.find_all()), 200

    @produto_ns.expect(produto)
    @produto_ns.doc('Create an produto')
    def post(self):
        produto_json = request.get_json()
        produto_data = produto_schema.load(produto_json)

        produto_data.save_to_db()

        return produto_schema.dump(produto_data), 201


class Item(Resource):

    def get(self, id):
        item_data = ItemModel.find_by_id(id)
        if item_data:
            return item_schema.dump(item_data)
        return {'message': ITEM_NOT_FOUND}, 404

    def delete(self, id):
        item_data = ItemModel.find_by_id(id)
        if item_data:
            item_data.delete_from_db()
            return '', 204
        return {'message': ITEM_NOT_FOUND}, 404

    @item_ns.expect(item)
    def put(self, id):
        item_data = ItemModel.find_by_id(id)
        item_json = request.get_json()

        if item_data:
            item_data.seq = item_json['seq']
            item_data.qtd = item_json['qtd']
            item_data.valor_item = item_json['valor_item']
        else:
            item_data = item_schema.load(item_json)

        item_data.save_to_db()
        return item_schema.dump(item_data), 200


class ItemList(Resource):
    @item_ns.doc('Get all the produtos.')
    def get(self):
        return item_list_schema.dump(ItemModel.find_all()), 200

    @item_ns.expect(item)
    @item_ns.doc('Create an item')
    def post(self):
        item_json = request.get_json()
        item_data = item_schema.load(item_json)

        item_data.save_to_db()

        return item_schema.dump(item_data), 201


class NotaFiscal(Resource):

    def get(self, id):
        nota_fiscal_data = NotaFiscalModel.find_by_id(id)
        if nota_fiscal_data:
            return nota_fiscal_schema.dump(nota_fiscal_data)
        return {'message': ITEM_NOT_FOUND}, 404

    def delete(self, id):
        nota_fiscal_data = NotaFiscalModel.find_by_id(id)
        if nota_fiscal_data:
            nota_fiscal_data.delete_from_db()
            return '', 204
        return {'message': ITEM_NOT_FOUND}, 404

    @nota_fiscal_ns.expect(nota_fiscal)
    def put(self, id):
        nota_fiscal_data = NotaFiscalModel.find_by_id(id)
        nota_fiscal_json = request.get_json()

        if nota_fiscal_data:
            nota_fiscal_data.codigo = nota_fiscal_json['codigo']
            nota_fiscal_data.data = nota_fiscal_json['data']
            nota_fiscal_data.valorNota = nota_fiscal_json['valorNota']
        else:
            nota_fiscal_data = nota_fiscal_schema.load(nota_fiscal_json)

        nota_fiscal_data.save_to_db()
        return nota_fiscal_schema.dump(nota_fiscal_data), 200


class NotaFiscalList(Resource):
    @nota_fiscal_ns.doc('Get all the notas.')
    def get(self):
        return nota_fiscal_schema.dump(NotaFiscalModel.find_all()), 200

    @nota_fiscal_ns.expect(nota_fiscal)
    @nota_fiscal_ns.doc('Create an nota fiscal')
    def post(self):
        nota_fiscal_json = request.get_json()
        nota_fiscal_data = nota_fiscal_schema.load(nota_fiscal_json)

        nota_fiscal_data.save_to_db()

        return item_schema.dump(nota_fiscal_data), 201
