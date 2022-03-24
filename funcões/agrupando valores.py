from itertools import groupby, tee

alunos = [
    {'nome': 'Luccas', 'nota': 'A'},
    {'nome': 'Bruno', 'nota': 'B'},
    {'nome': 'Lais', 'nota': 'C'},
    {'nome': 'Neymar', 'nota': 'C'},
    {'nome': 'Sergio', 'nota': 'A'},
    {'nome': 'Patricia', 'nota': 'B'},
    {'nome': 'Joana', 'nota': 'B'},
    {'nome': 'Bernardo', 'nota': 'C'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Rayane', 'nota': 'A'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados=groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    print(agrupamento)
    for aluno in va1:
        print(f'- {aluno["nome"]}')
    qnt = len(list(va2))
    print(f'{qnt} alunos')