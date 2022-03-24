usuario = input('Nome de usuário: ')
senha = input('Digite a sua senha: ')

usuario_bd = "alberto"
senha_bd = "123456"

if usuario == usuario_bd and senha == senha_bd:
    print("Você está logado.")
else:
    print("Usuário ou senha inválidos.")