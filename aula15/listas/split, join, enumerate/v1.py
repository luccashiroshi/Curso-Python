"""
split, join e enumerate
*split - dividir uma string # str
*join - juntar uma lista # str
*enumerate - enumerar elementos da lista # list
"""
string = "o Brasil é o país do futebol, o Brasil é penta."
lista1 = string.split(' ')
lista2 = string.split(',')

word = ''
cont = 0
for valor in lista1:
    qtd = lista1.count(valor)

    if qtd > cont:
        cont = qtd
        word = valor

print(f'A palavra que mais apareceu foi "{word}" ({cont}x)')
