nome = input("Digite seu primeiro nome: ")

if len(nome) <= 4:
    print(f'Seu nome é curto!')
elif 5 <= len(nome) <= 6:
    print(f'Seu nome é normal!')
else:
    print('Seu nome é muito grande!')