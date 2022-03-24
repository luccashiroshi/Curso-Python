"""
Listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
lista = ['Amora', 'Batata', 'Cana', 'Dado', 'Escola']
print(lista[1])
lista[1] = "macarraao"
print(lista[1])
print(lista[2:5])

l1 = [1, 2, 3, 4]
l2 = [7, 8, 9, 0]
l3 = l1 + l2

print(l1)
print(l2)
print(l3)

l1.extend(l2) # extende até l2

print(l1)

l2.append("luccas")  # insere novo valor no final da lista

print(l2)

l1.insert(0, "macaco")  # insere na posição indicada

print(l1)

print(l2)
l2.pop()  # remove o ultimo elemento
print(l2)

l4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l4)
del(l4[0:9:2])  # remove um intervalo
print(l4)

l5 = list(range(1, 21))
print(l5)

for valor in l5:
    print(valor)

for elem in l1:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')

print("-----------------------------------------------------------")
