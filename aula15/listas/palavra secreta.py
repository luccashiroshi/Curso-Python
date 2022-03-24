import random
l1 = ["abacate", "berimbau", "ornitorrinco", "hipopotamo"]
secreto = l1[random.randint(0, 4)]
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print("Você Perdeu!")
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta')
    else:
        print(f'A letra "{letra}" não existe na palavra secreta')
        digitadas.pop()

    secreto_temporario = ""
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f'Você ganhou!! A palavra era {secreto_temporario}')
        break
    else:
        print(secreto_temporario)

    if letra not in secreto:
        chances -= 1

    print(f'você ainda tem {chances} chances.')
    print()
