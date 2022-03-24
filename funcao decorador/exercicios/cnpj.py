from functools import reduce
base = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def first(lista):
    soma = reduce(lambda ac, p: p+ac, lista, 0)
    valor = 11 - (soma % 11)
    st_dig = 0 if valor > 9 else valor
    return str(st_dig)


def second(lista):
    soma = reduce(lambda ac, p: p + ac, lista, 0)
    valor = 11 - (soma % 11)
    st_dig = 0 if valor > 9 else valor
    return str(st_dig)


while True:
    cnpj = input('Digite seu CNPJ: ')
    try:

        cnpj_list = [n for n in cnpj]

        formated_cnpj = filter(lambda n: n.isnumeric(), cnpj_list)
        formated_cnpj = list(formated_cnpj)

        produto = map(lambda c, b: int(c)*b, formated_cnpj[:12], base[1:])

        new_formated_cnpj = formated_cnpj[:12]
        new_formated_cnpj.append(first(produto))

        produto2 = map(lambda c, b: int(c)*b, new_formated_cnpj, base)

        new_formated_cnpj.append(second(produto2))

        msg = "Número de CNPJ válido!"if new_formated_cnpj == formated_cnpj else "Número de CNPJ inválido!"

        print(msg)

    except Exception:
        print('Error')
    finally:
        continue