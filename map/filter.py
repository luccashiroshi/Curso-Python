from dados import produtos, pessoas, lista
from functools import reduce

def filtra(produto):
    if produto['preco'] > 50:
        return True


def filtra_idade(pessoa):
    if pessoa['idade'] >= 18:
        return True
    return False


nova_lista = filter(filtra, produtos)
nova_lista1 = filter(filtra_idade, pessoas)

for produto in nova_lista:
    print(produto)

print('----------------------------------------------')

for pessoa in nova_lista1:
    print(pessoa)

print('----------------------------------------------')

# acumula = 0
#
# for item in lista:
#     acumula+=item
#     print(acumula)

soma_lista = reduce(lambda ac, i: i+ac, lista, 0)
print(soma_lista)

print('----------------------------------------------')

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)

print(round(soma_precos / len(produtos), 2))

print('----------------------------------------------')

soma_idades = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)
print(soma_idades / len(pessoas))
