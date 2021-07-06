from app.app import Cliente
from app import db

def instanciar():
    cl1 = Cliente(1,
                  'Yury',
                  10,
                  '1234567890',
                  'P. Física')
    db.session.add(cl1)
    db.session.commit()
