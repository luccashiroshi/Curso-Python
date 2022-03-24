nome = "luccas"  # variável assume o valor Luccas
idade = 17
altura = 1.75
e_maior = idade > 18
peso = 80
imc = peso / altura ** 2

print(nome)
print(idade)
print(altura)
print(e_maior)

print(nome, 'tem', idade, 'de idade e seu imc é', imc)

print(f'{nome} tem {idade} anos e seu imc é {imc:.2f}')

print('{} tem {} anos de idade e seu imc é {:.2f}'. format(nome, idade, imc))
