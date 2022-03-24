from datetime import datetime
from locale import setlocale, LC_ALL


def dataptbr(data):
    setlocale(LC_ALL, 'pt_BR.utf-8')
    formata = data.strftime('%A, %d de %B de %Y')
    print(formata)


def dataeng(data):
    setlocale(LC_ALL, 'eng_US.utf-8')
    formata = data.strftime('%A, %d de %B de %Y')
    print(formata)


dataptbr(datetime.now())
dataeng(datetime.now())
