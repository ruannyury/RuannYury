"""
Pilha (inserir e retirar pelo topo da Pilha. Considerar o topo como sendo o índice 0 da Lista.
"""
pilha = []

for x in range(1, 11):
    pilha.insert(0, x)

print(pilha)

for x in range(11, 1, -1):
    print(pilha)
    pilha.pop(0)

print(pilha)
