"""
Funcões - def em Python
"""


# def funcao(msg = "olá", nome = "Usuário"):
#     print(msg, nome)
# funcao("Olá", "Luccas")
# funcao("oi", "bruno")
# funcao("Olá", "Luccas")
# funcao()

def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2


divide = divisao(8, 5)

if divide:
    print(divide)
else:
    print("conta inválida")
