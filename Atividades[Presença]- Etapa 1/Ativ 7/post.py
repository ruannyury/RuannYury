class Post:
    def __init__(self, nome, legenda, foto_post):
        self._nome = nome
        self._legenda = legenda
        self._foto_post = foto_post

    def postar(self):
        _str = """
        {}|| {}
        {}
        """.format(self._nome,
                   self._legenda,
                   self._foto_post)
        return _str

    def altera_legenda(self, legenda):
        self._legenda = legenda

    def altera_foto_post(self, foto):
        self._foto_post = foto
