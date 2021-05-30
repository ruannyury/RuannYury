"""
Codifique classes a partir do modelo de domínio gerado da atividade anterior.
Crie classes onde seja possível estabelecer os relacionamentos abordados mas aulas.
"""


class Usuario:
    def __init__(self, nome, email, telefone):
        self._nome = nome
        self._email = email
        self._telefone = telefone

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email

    def get_telefone(self):
        return self._telefone

    def altera_nome(self, nome):
        self._nome = nome

    def altera_email(self, email):
        self._email = email

    def altera_telefone(self, telefone):
        self._telefone = telefone
