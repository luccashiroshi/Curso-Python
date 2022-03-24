"""
combinations, permutations e product - Itertools
combinação - ordem não importa
permutação - ordem importa
ambos nao repetem valores unicos
produto - ordem importa e repete valores unicos
"""
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

for grupo in combinations(pessoas, 2):
    print(grupo)

print('--------------------------------------------')

for grupo in permutations(pessoas, 2):
    print(grupo)

print('--------------------------------------------')

for grupo in product(pessoas, repeat=2):
    print(grupo)