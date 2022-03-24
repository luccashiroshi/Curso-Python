lista_de_tarefas = []
backup = []


def listar(lista_de_tarefas):
    for tarefa in lista_de_tarefas:
        print(f'-{tarefa}')


def apagar(lista, backup):
    lista_de_tarefas.pop()
    return lista_de_tarefas

def refazer(lista, backup):
    pass


def adicionar(lista, backup):
    lista_de_tarefas.append(input('Nova tarefa: '))
    last = lista_de_tarefas.pop()
    backup.append(last)
    return lista_de_tarefas, backup


while True:
    decision = input('[N] Nova Tarefa\n[L] Listar Tarefas \n[D] Deletar Tarefa \n[R] Refazer\n')
    if decision == 'n' or decision == 'N':
        adicionar(lista_de_tarefas, backup)
        continue
    elif decision == 'l' or decision == 'L':
        listar(lista_de_tarefas)
        continue
    elif decision == 'd' or decision == 'D':
        apagar(lista_de_tarefas, backup)
        continue
    elif decision == 'r' or decision == 'R':
        refazer(lista_de_tarefas, backup)
        continue

