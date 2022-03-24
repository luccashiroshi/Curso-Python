from pessoa import Pessoa

p1 = Pessoa('Luccas', 18)
p2 = Pessoa('Roberval', 57)

p1.comer('carne')
p1.falar('emprego')
p2.falar('emprego')
p2.comer('mamão')
p2.falar('escola')
p2.parar_falar()
p1.get_ano_nascimento()
p2.get_ano_nascimento()

#  class method
p3 = Pessoa.por_ano_nascimento('Claudia', 1975)
print(p3.nome, p3.idade)

print(p1.gera_id())
print(p2.gera_id())
print(p3.gera_id())
