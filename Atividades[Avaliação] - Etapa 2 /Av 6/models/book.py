from db import db
from typing import List
import datetime


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

    notafiscal = db.relationship("NotaFiscalModel", back_populates="clientes", uselist=False)

    def __init__(self, nome, codigo, cnpjcpf, tipo):
        self.nome = nome
        self.codigo = codigo
        self.cnpjcpf = cnpjcpf
        self.tipo = tipo

    def __repr__(self):
        return f'ClienteModel(nome={self.nome}, codigo={self.codigo}, cnpjcpf={self.cnpjcpf}, tipo={self.tipo})'

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


class ProdutoModel(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(160), nullable=False)
    valor_unidade = db.Column(db.Float, nullable=False)

    item = db.relationship("ItemModel", back_populates="produtos", uselist=False)

    def __init__(self, descricao, valor_unidade):
        self.descricao = descricao
        self.valor_unidade = valor_unidade

    def __repr__(self):
        return f'ProdutoModel(descrição={self.descricao}, valor_unitario={self.valor_unidade}'

    def json(self):
        # return {'title': self.title, 'pages': self.pages}
        return {'descricao': self.descricao,
                'valor_unidade': self.valor_unidade}

    @classmethod
    def find_all(cls) -> List["ProdutoModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id) -> "ProdutoModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()


class ItemModel(db.Model):
    __tablename__ = 'itens'
    id = db.Column(db.Integer, primary_key=True)
    seq = db.Column(db.Integer, nullable=False)
    qtd = db.Column(db.Integer, nullable=False)

    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'))
    produto = db.relationship('ProdutoModel', back_populates='itens')

    def __init__(self, seq, qtd):
        # self.id = id
        self.seq = seq
        self.qtd = qtd
        self.valor_item = float(self.qtd * self.produto.valor_unidade)
        # self.produto = produto
        # self.descricao = descricao
        # self.valor_unitario = self.produto.valor_unidade

    def __repr__(self):
        return f'ItemModel(sequencial={self.seq}, quantidade={self.qtd}, valor_item={self.valor_item}'

    def json(self):
        # return {'title': self.title, 'pages': self.pages}
        return {'sequencial': self.seq,
                'quantidade': self.qtd,
                'valor_item': self.valor_item}

    @classmethod
    def find_all(cls) -> List["ItemModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id) -> "ItemModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()


class NotaFiscalModel(db.Model):
    __tablename__ = 'notafiscal'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer, nullable=False, unique=True)

    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    cliente = db.relationship('ClienteModel', back_populates='notafiscal')

    def __init__(self, codigo):
        # self.id = id
        self.codigo = codigo
        # self.cliente = cliente
        self.data = datetime.datetime.now()
        self.itens = []
        self.valorNota = 0.0

    def __repr__(self):
        return f'NotaFiscalModel(codigo={self.seq}, data={self.data_nota()}, valor_nota={self.valorNota}'

    def json(self):
        # return {'title': self.title, 'pages': self.pages}
        return {'sequencial': self.seq,
                'quantidade': self.qtd,
                'valor_item': self.valor_item}

    @classmethod
    def find_all(cls) -> List["NotaFiscalModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id) -> "NotaFiscalModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def data_nota(self):
        lista_data_e_hora = str(self.data).split()  # Separa o resultado de "datetime.datetime.now()" numa lista
        # com 2 elementos, a data e a hora
        data_lista = lista_data_e_hora[0].split('-')  # Divide em strings apenas a data, primeiro elemento da lista
        # acima
        data_final_nota = f'{data_lista[2]}/{data_lista[1]}/{data_lista[0]}'  # Ordena a data na nossa ordem padrão
        return data_final_nota  # Retorna a data formatada

    def adicionar_item(self, item):
        if isinstance(item, ItemModel):
            self.itens.append(item)

    def calcular_total_nota(self):
        valor = 0.0
        for item in self.itens:
            valor = valor + item.valor_item
        self.valorNota = valor
        return self.valorNota

    def get_valor_nota(self):
        return self.valorNota

    def imprimir_nota_fiscal(self):
        """
        Formatação final da nota fiscal, a string completa de saída. Método principal do programa.
        """
        linhas = '-' * 111

        formatacao_nota = '{}\n' \
                          'NOTA FISCAL{:>100}\n' \
                          'Cliente:{:>6}{:>4}Nome: {}\n' \
                          'CPF/CNPJ: {}\n' \
                          '{}\n' \
                          'ITENS\n' \
                          '{}\n' \
                          'Seq{:>3}Descricao{:>52}QTD{:>7}Valor Unit{:19}Preço\n' \
                          '{}  {}    {}     {}     {}'.format(linhas,
                                                              self.data_nota(),
                                                              self.cliente.codigo, ' ', self.cliente.nome,
                                                              self.cliente.cnpjcpf,
                                                              linhas,
                                                              linhas,
                                                              ' ', ' ', ' ', ' ',
                                                              '-' * 4, '-' * 56, '-' * 5, '-' * 12, '-' * 18)

        if len(self.itens) > 0:  # Adicionando e formatando os itens, elementos finais da nota
            for item_nota in self.itens:
                formatacao_nota += '\n\n{}{:>3}{}'.format(item_nota.seq, ' ', item_nota.produto.descricao)
                formatacao_nota += ' ' * (60 - len(item_nota.produto.descricao))  # Controlando de acordo com a
                # descrição
                formatacao_nota += '{:.2f}             {:.2f}                  {:.2f}'.format(
                    item_nota.qtd, item_nota.produto.valor_unidade,
                    item_nota.valor_item)

        formatacao_nota += '\n{}\nValor Total: {:.2f}'.format(linhas, self.valorNota)  # Ou calcular_total_nota()
        return formatacao_nota                                                         # get_valor_nota()
