# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estao nos dois sets, mas nao em ambos)

s1 = {1, 2, 3, 4, 5, 6}
s2 = set()  # set vazio
s2.add((5, 2, 7, 8))
print(s2)
s1.discard(6)
print(s1)
s1.update([1, 2, 3, 4, 5], {5, 6, 7, 8})
print(s1)

s3 = {1, 2, 3, 4, 5}
s4 = {1, 2, 3, 4, 5, 6, 7, 8}
s5 = s3 | s4

print(s5)

s5 = s3 & s4

print(s5)

s5 = s4 - s3

print(s5)

s5 = s3 ^ s4

print(s5)
