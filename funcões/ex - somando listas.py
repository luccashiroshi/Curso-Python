lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4]

listasoma = [x + y for x, y in zip(lista1, lista2)]
print(list(listasoma))
