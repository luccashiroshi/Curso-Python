"""
operadores lógicos
and, or, not
in e not in
"""

num = int(input("Número: "))

if num % 2 == 0 and num % 3 == 0:
    print(f"é divisível por 6")
elif not num % 2 == 0 and not num % 3 == 0:
    print(f"não é divisível por 6")
elif num % 2 == 0:
    print(f"é divisível somente por 2")
elif num % 3 == 0:
    print(f"é divisível somente por 3")
else:
    print(f"não é divisível por 2, 3 ou 6")

nome = input("digite seu nome: ")

# se lu existir dentro da variavel nome
if "lu" in nome:
    print('existe o texto')
else:
    print('não existe o texto')
    