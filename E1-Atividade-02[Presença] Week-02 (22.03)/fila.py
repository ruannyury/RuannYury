# Fila (Inserir no final da Fila. Considerar o final da fila o elemento de maior índice positivo.
# Retirar da Fila pelo elemento do inicio da Lista que tem o índice 0.)
fila = [1, 2, 3, 4]
print(fila)

for x in range(5, 8):
    fila.append(x)
print(fila)

for i in range(1, 8):
    print(fila)
    fila.pop(0)
