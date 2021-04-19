"""
O código Morse é um esquema de
codificação que usa travessões e pontos para representar dígitos e letras.
Nesta atividade, você escreverá um programa que usa um dicionário para
armazenar o mapeamento desses símbolos para o código Morse. Use um ponto para
representar um ponto e um hífen para representar um travessão. O mapeamento de
caracteres para travessões e pontos é mostrado na Tabela definida no arquivo CodigoMorse-02.jpg.
Seu programa deve ler uma mensagem do usuário. Em seguida, deve traduzir todas as letras e dígitos da
mensagem para o código Morse, deixando um espaço entre cada sequência de
travessões e pontos. Seu programa deve ignorar quaisquer caracteres que não
estejam listados na tabela anterior.
"""

dicionario_de_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                       'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                       'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                       'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                       '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

print('ESCREVA UMA MENSSAGEM PARA SER TRADUZIDA EM CÓDIGO MORSE:')
mensagem_normal = input('Mensagem: ')

caracteres = []
for x in range(len(mensagem_normal)):  # Percorrer toda a mensagem
    caractere = mensagem_normal[x].lower()  # Caso haja caracteres maiúsculos, deixa-os minúsculos primeiro
    if caractere in dicionario_de_morse.keys():  # para só então pesquisá-los no dicionário
        caracteres.append(caractere)  # Caso esteja no dicionário, é adicionado na lista de caracteres para ser mapeada
    # em seguida

traducao = list(map(lambda c: dicionario_de_morse[c], caracteres))  # Mapea todos os caracteres da lista criada e
# retorna o seu respectivo caractere em morse noutra lista
mensagem_traduzida = ' '.join(traducao)  # Transforma a lista de tradução numa string normal
print(f'A mensagem traduzida em código morse é: {mensagem_traduzida}')  # Exibe a mensagem traduzida
