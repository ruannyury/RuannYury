"""O triângulo pode ser classificado com base no comprimento de
seus lados em equilátero, isósceles ou escaleno. Todos os três lados de um
triângulo equilátero têm o mesmo comprimento. Um triângulo isósceles tem dois
lados que são do mesmo comprimento e um terceiro lado que é diferente comprimento.
Se todos os lados tiverem comprimentos diferentes, o triângulo é escaleno.
Escreva um programa que leia os comprimentos dos três lados de um triângulo do usuário.
Em seguida, exiba uma mensagem que declara o tipo do triângulo."""

print('Verificaremos se o triângulo é equilátero, isósceles ou escaleno a partir do tamanho dos lados inserido.')

a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))

if a == b and b == c:
    print('O triângulo é equilátero')
elif a == b or a == c or b == c:
    print('O triângulo é isósceles')
else:
    print('O triângulo é escaleno')
