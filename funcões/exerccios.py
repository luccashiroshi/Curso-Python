quebra = "-----------------------------------------------------------------------"


# ex 1
def func(saudacao="Olá", nome="usuário"):
    print(f'{saudacao} {nome}!')


func(nome=input("Digite seu Nome: "))

print(quebra)


# ex 2

def soma(x, y, z):
    try:
        x = int(x)
        y = int(y)
        z = int(z)

        return print(x + y + z)
    except:
        return print("Número Inválido.")


soma(x=input("Primeiro número: "), y=input("Segundo número: "), z=input("Terceiro número: "))

print(quebra)

# ex 3


def percent(num, porc):
    try:
        num = int(num)
        porc = int(porc)
        return print(num + num * (porc/100))
    except:
        return print("Não foi possível obter resultado.")


percent(num=input("Primeiro valor: "), porc=input("Aumento percentual: "))

print(quebra)

# ex 4


def fizzbuzz(par):
    if par % 5 == 0 and par % 3 == 0:
        return "FizzBuzz"
    if par % 3 == 0:
        return "fizz"
    if par % 5 == 0:
        return "buzz"
    return par


print(fizzbuzz(int(input("Digite um Número: "))))

