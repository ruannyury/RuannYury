from func_verificacao import verificacao

print('Insira 3 lados e verificaremos se é possível formar um triângulo com eles.')

a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))

if verificacao(a, b, c):  # Chama a função
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')
