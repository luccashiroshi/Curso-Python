# condições IF, ELIF e ELSE
"""
Operadores Relacionais
== > >= < <= !=
retornam um valor bool
"""

num_1 = int(input("Número 1: "))
num_2 = int(input("Número 2: "))

if num_1 > num_2:
    print(f'{num_1} > {num_2}')
elif num_1 < num_2:
    print(f'{num_1} < {num_2}')
else:
    print("Os números são iguais")
