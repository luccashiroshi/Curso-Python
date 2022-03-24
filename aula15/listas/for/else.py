"""
for/else em pythom
"""

variavel = ['Luccas', "Rayane", "Pedro", "Bruno"]
cond = False
letra = input("Digite uma letra: ")
for valor in variavel:
    if valor.lower().startswith(letra):
        print(valor)
    elif len(letra) > 1:
        print('ERROR')
        break
else:
    print(f'Não existe palavra com a letra {letra}.')
