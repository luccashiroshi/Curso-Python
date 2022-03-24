
# def gera():
#     for n in range(100):
#         yield n
#
#
# g = gera()
#
# for v in g:
#     print(v)

l1 = [x for x in range(1000)]  # lista
l2 = (x for x in range(1000))  # Gerador ocupa menos espaço na memória

for v in l2:
    print(v)
