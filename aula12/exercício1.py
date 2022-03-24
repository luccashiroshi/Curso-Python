num = input("Digite um número inteiro: ")

try:

    num = int(num)

    if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é ímpar')

except:
    print(f'{num} não é um número inteiro')
