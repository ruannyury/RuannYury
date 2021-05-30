from usuario import Usuario
from perfil import Perfil
from post import Post


user1 = Usuario('Ruann', 'ruannyury1@outlook.com', '85988994070')

perfil_user1 = Perfil(user1.get_nome(), user1.get_email(),
                      user1.get_telefone(),
                      'foto.png', 'Essa é a minha descrição!')

post_user1 = Post(user1.get_nome(), 'Este é meu primeiro post!', 'primeiropost.png')
post2_user1 = Post(user1.get_nome(), 'Este é meu segundo post!', 'segundopost.png')
post3_user1 = Post(user1.get_nome(), 'Este é meu terceiro post!', 'terceiropost.png')
