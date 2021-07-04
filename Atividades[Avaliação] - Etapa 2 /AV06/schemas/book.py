from ma import ma
from models.book import BookModel, ClienteModel, ProdutoModel, ItemModel, NotaFiscalModel


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookModel
        load_instance = True


class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ClienteModel
        load_instance = True


class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProdutoModel
        load_instance = True


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemModel
        load_instance = True


class NotaFiscalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NotaFiscalModel
        load_instance = True
