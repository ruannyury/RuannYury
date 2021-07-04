from flask import Flask, Blueprint, jsonify
from flask_restplus import Api
from ma import ma
from db import db

from resources.book import Book, BookList, book_ns, Cliente, ClienteList, Produto, ProdutoList, Item, ItemList, \
    NotaFiscal, NotaFiscalList
from marshmallow import ValidationError

from server.instance import server

api = server.api
app = server.app


@app.before_first_request
def create_tables():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


api.add_resource(Book, '/books/<int:id>')
api.add_resource(BookList, '/books')

api.add_resource(Cliente, '/clientes/<int:id>')
api.add_resource(ClienteList, '/clientes')

api.add_resource(Produto, '/produtos/<int:id>')
api.add_resource(ProdutoList, '/produtos')

api.add_resource(Item, '/itens/<int:id>')
api.add_resource(ItemList, '/itens')

api.add_resource(NotaFiscal, '/notas/<int:id>')
api.add_resource(NotaFiscalList, '/notas')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()
