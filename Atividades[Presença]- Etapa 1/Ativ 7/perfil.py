class Perfil:
    def __init__(self, nome, email, telefone, foto, descricao):
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._foto = foto
        self._descricao = descricao
        self._posts = []

    def mostra_perfil(self):
        dados_perfil = [self._foto, self._nome, self._email, self._telefone,
                        self._descricao]
        for dado in dados_perfil:
            print(dado)

    def adicionar_posts(self, post):
        self._posts.append(post)

    def listar_posts(self):
        print("==================LISTA DE POSTS==================")
        for post in self._posts:
            print(post, end='\n\n')

    def altera_foto(self, foto):
        self._foto = foto

    def altera_descricao(self, descricao):
        self._descricao = descricao
