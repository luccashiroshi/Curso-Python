usuario= input('Digite sua senha: ')
qnt = len(usuario)

print(f"{qnt} caracteres")
if qnt >= 8:
    print(f"senha aceita")
else:
    print(f"numero de caracteres insuficiente")