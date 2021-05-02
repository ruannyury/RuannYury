"""Para ganhar o prêmio máximo na Mega Sena, é necessário
acertar todos os 6 números em seu bilhete com os 6 números entre 1 e 60
sorteados. Escreva um programa que gere uma seleção aleatória de 6 números para
uma aposta. Certifique-se de que os 6 números selecionados não contenham
duplicatas. Exibir os números em ordem crescente."""

from random import randint

numeros_apostados = []

while len(numeros_apostados) < 6:  # Executa o loop até o número de apostas chegue em 6
    numero_aleatorio = randint(1, 60)  # Gera um número aleatório de 1 a 60
    if numero_aleatorio not in numeros_apostados:  # Verifica se esse número já foi apostado
        numeros_apostados.append(numero_aleatorio)  # Se não, é adicionado à aposta

numeros_apostados.sort()  # Ordena os números de forma crescente
print('Os números que você deve jogar são:', numeros_apostados)
