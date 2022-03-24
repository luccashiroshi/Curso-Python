# 1

def func():
    return "felicidadew"


def func2(funcao):
    return funcao()


varia = func2(func)
print(varia)

# 2


def fu1(nome, idsex):
    print(nome, idsex)


def fu2(nome):
    return f'oi {nome}'


def fu3(idade, sexo):
    return f'sexo: {sexo}, idade: {idade}'


nome = fu2('Alberto')
idsex = fu3(59, "masculino")
fu1(nome, idsex)
