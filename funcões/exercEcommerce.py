
carrinho = []

carrinho.append(('Produto 1', 45))
carrinho.append(('Produto 2', 25))
carrinho.append(('Produto 3', 50))

total = sum([preco[1] for preco in carrinho])
print(total)
