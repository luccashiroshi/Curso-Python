import random
from functools import reduce

base = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def first(lista):
    soma = reduce(lambda ac, p: p+ac, lista, 0)
    valor = 11 - (soma % 11)
    st_dig = 0 if valor > 9 else valor
    return st_dig


def second(lista):
    soma = reduce(lambda ac, p: p + ac, lista, 0)
    valor = 11 - (soma % 11)
    st_dig = 0 if valor > 9 else valor
    return st_dig


def formata(lista):
    cnpj = ''.join(str(v) for v in lista)
    formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatado


while True:
    cnpj = [random.randint(000000000000, 999999999999)]

    cnpj_list = [n for n in cnpj]

    produto = map(lambda c, b: int(c)*b, cnpj, base[1:])

    new_cnpj = cnpj[:12]
    new_cnpj.append(first(produto))

    produto2 = map(lambda c, b: int(c)*b, new_cnpj, base)

    new_cnpj.append(second(produto2))

    print(formata(new_cnpj))
    decision = input("[Enter] Novo CNJP\n[s] Sair\n")
    if decision == 's':
        break
    else:
        continue
