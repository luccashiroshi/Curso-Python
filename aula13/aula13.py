"""
Formatando valores com modificadores

:s - (texto strings)
:d - inteiros (int)
:f - numeros ponto flutuante (float)
:.(NÚMERO)f - quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - esquerda
< - direita
^ - centro

"""

num1 = 10
num2 = 3
divisao = num1 / num2
print( '{:.2f}'.format(divisao) )

num = 1
print(f'{num:0>10}')  # variável num vai ser escrita com 9 zeros completando à esquerda

num3 = 1245
print(f'{num3:0<10}')
print(f'{num3:0^10}')
print(f'{num3:0>10.2f}')

nome = "Luccas"
sobrenome = "hina"
print(f'{nome:*^50}')
nome_formatado = '{0:0^20}{1}'.format(nome, sobrenome)
print(nome_formatado)

print(nome.lower())  # tudo minusculo
print(nome.upper())  # tudo maiusculo
print(nome.title())  # primeiras letras maiusculas

