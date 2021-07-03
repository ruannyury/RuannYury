from db import db
from typing import List


class BookModel(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    pages = db.Column(db.Float(precision=2), nullable=False)

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __repr__(self):
        return f'BookModel(title={self.title}, pages={self.pages})'

    def json(self):
        return {'title': self.title, 'pages': self.pages}

    @classmethod
    def find_by_title(cls, title) -> "BookModel":
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_by_id(cls, _id) -> "BookModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["BookModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()


class ClienteModel(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(160), nullable=False, unique=True)
    codigo = db.Column(db.Integer, nullable=False, unique=True)
    cnpjcpf = db.Column(db.String(160), nullable=False, unique=True)
    tipo = db.Column(db.String(160), nullable=False)

    def __init__(self, nome, codigo, cnpjcpf, tipo):
        self.nome = nome
        self.codigo = codigo
        self.cnpjcpf = cnpjcpf
        self.tipo = tipo

    def __repr__(self):
        return f'Cliente(nome={self.nome}, codigo={self.codigo}, cnpjcpf={self.cnpjcpf}, tipo={self.tipo})'

    def json(self):
        # return {'title': self.title, 'pages': self.pages}
        return {'nome': self.nome,
                'codigo': self.codigo,
                'cnpjcpf': self.cnpjcpf,
                'tipo': self.tipo}

    @classmethod
    def find_all(cls) -> List["ClienteModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id) -> "ClienteModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
