def func(*args, **kwargs):
    print(args)
    print(kwargs)

    idade = kwargs.get('idade')
    if idade:
        print(kwargs["idade"])
    else:
        print("idade não existe")


lista1 = [10, 20, 30, 40, 50]
lista = [1, 2, 3, 4, 5]
func(*lista, *lista1, nome='Luccas', sobrenome="Hina", idade=15)
