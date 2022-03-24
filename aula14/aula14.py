"""
while em python
utilizado para realizar ações enquanto a condição for verdaeira
"""
a = 0
"""
while a <= 100:  # enquanto a for menor que 100
    print(a)
    a = a + 1  # a cada loop é adicionado 1 ao valor de a

print('acabou!')
"""

x = 0  # colunas
while x < 10:
    y = 0  # linhas

    while y <= 5:
        print(f'({x}, {y})')
        y += 1

    x += 1

print('Acabou!')
