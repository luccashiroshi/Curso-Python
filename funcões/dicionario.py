
# d1 = {'chave1':'valor da chave'}
d1 = dict(chave1='valor da chave', chave2='valor da outra chave')

print(d1['chave1'])

d1['novaChave'] = "auau"  # adicionar nova chave
print(d1)
del d1['novaChave']  # apagar chave
print(d1)

print("chave1" in d1)
print('auau' in d1)
print('valor da chave' in d1.values())

for k in d1:
    print(k)

for k in d1.values():
    print(k)
for k, v in d1.items():
    print(k, v)

clientes = {
    'cli1': {
        'nome': 'Luiz',
        'sobrenome': 'Inácio'
    },
    'cli2': {
        'nome': 'Carlos',
        'sobrenome': 'Ferreira'
    },
}
print("-----------------------------------------------------------------------")
for clientes_k, clientes_v in clientes.items():
    print(f'exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
