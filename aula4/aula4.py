"""
Tipo de map
str - string - textos 'assim' "assim"
int - inteiro - 12345 0 -10 -20 -50 -15000
float - real/ponto flutuante - 10.50 1.5 -12.5
bool - booleano/lógico - True/False
"""

print('luccas', type('luccas'))  # descobrir o tipo de texto
print(10, type(10))
print(10.45, type(10.45))
print(10 == 45, type(10 == 45))
print(45 == 45, type(45 == 45))

print(10+10)
print('10'+'10')

# Nome: str
print('Luccas Hiroshi', type('Luccas Hiroshi'))

# Idade: int
print(17, type(17))

# Altura: float
print(1.75, type(1.75))

# É maior de idade: bool
print(17 < 18, type(17 > 18))

