def master(funcao):
    def slave():
        print('agr estou decorada')
        funcao()
    return slave


@master
def fala_oi():
    print('Oi')


# fala_oi = master(fala_oi)
fala_oi()

