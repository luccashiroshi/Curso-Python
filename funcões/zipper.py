"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""

from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Francisco Morato']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(indice, estados, cidades)

cidades_estados2 = zip_longest(estados, cidades, fillvalue='Estado')
print(list(cidades_estados2))
for indice, cidades, estados in cidades_estados:
    print(indice, cidades, estados)
