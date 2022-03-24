"""
CPF = 482.159.628-82
"""
cpf = input("Digite seu CPF: ")
digitos = cpf[:11].replace(".", "")
numCPF = digitos + cpf[12:14]
soma1 = 0
soma2 = 0
for digIndex, value in enumerate(range(10, 1, -1)):
    x = int(digitos[digIndex])
    y = x * value
    soma1 += y

d1 = 0 if 11 - (soma1 % 11) > 9 else 11 - (soma1 % 11)

digit1 = digitos + str(d1)

for digIndex2, value2 in enumerate(range(11, 1, -1)):
    x1 = int(digit1[digIndex2])
    y1 = x1 * value2
    soma2 += y1

d2 = 0 if 11 - (soma2 % 11) > 9 else 11 - (soma2 % 11)

novo_cpf = digit1 + str(d2)
print("Número de CPF Válido!") if novo_cpf == numCPF else print("Número de CPF Inválido!")
