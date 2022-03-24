
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2?',
        'respostas': {'a': '12', 'b': '10', 'c': '8'},
        'resposta_certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 256/2?',
        'respostas': {'a': '133', 'b': '56', 'c': '128'},
        'resposta_certa': 'c',
    },
    'Pergunta 4': {
        'pergunta': 'O que é? O que é? Entra duro e sai pingando?',
        'respostas': {'a': 'Gelo', 'b': 'Batom', 'c': 'Guarda-chuva'},
        'resposta_certa': 'a',
    },
    'Pergunta 5': {
        'pergunta': 'Qual é a capital do Brasil?',
        'respostas': {'a': 'Maceió', 'b': 'Brasília', 'c': 'São Paulo'},
        'resposta_certa': 'b',
    },
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Respostas: ')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print("Acertou!!")
        respostas_certas += 1
    else:
        print("Errada!")
    print()

qntd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qntd_perguntas * 100
print(f'Você acertou {respostas_certas}  respostas.')
print(f'Sua porcentagem de acertos foi de {porcentagem_acerto}%')
