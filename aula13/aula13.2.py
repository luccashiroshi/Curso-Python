"""
Manipulando strings
*String indices
*fatiamento de strings [inicio:fim:passo]
*funções built-in len, abs, type, print, etc...
"""
# positivos [012345678]

texto = 'Python_s2'

#negativo -[987654321]

print(texto[8])  # pega o nono caractere da string
print(texto[-1])

nova_string = texto[2:6]  # pega o caractere na posição 2 até o 5
nova_string2 = texto[:6]  # pega o caractere do começo até o 5
nova_string3 = texto[0::3]  # pega o caractere do começo até o ultimo pulando 3 caracteres entre eles
print(nova_string)
print(nova_string2)
print(nova_string3)