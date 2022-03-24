# Módulos padrão Python:
# Módulos são arquivos .py (que contem código python) e servem para expandir as funcionalidades padrão da linguagem.

# import sys       #  importa o módulo inteiro
# print(sys.platform)
from sys import platform as so  # importa o módulo e renomeia
import random

print(so)

for i in range(10):
    print(random.randint(0, 10))
