"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""
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

print(idade * altura)
print(idade * nome)

print(nome, 'tem', idade, 'de idade e seu imc é', imc)
