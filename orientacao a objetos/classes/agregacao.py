from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 30)
p2 = Produto('Iphone', 3500)
p3 = Produto('Faca', 5)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produtos()
print(carrinho.soma_total())
