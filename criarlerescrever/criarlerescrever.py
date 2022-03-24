import os

# os.remove('abc.txt')   apaga o arquivo

file = open('abc.txt', 'w+')
file.write('linha 1\n')
file.write('linha 2\n')
file.write('linha 3\n')


file.seek(0, 0)
print(file.read())

print('---------------------------')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

print('---------------------------')

file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='')

file.close()

print('---------------------------')

with open('bda.txt', 'w+') as file2:
    file2.write('Cabecinha\n')
    file2.write('de\n')
    file2.write('Guidão\n')

    file2.seek(0)
    print(file2.read())

with open('bda.txt', 'r') as file2:
    print(file2.read())

with open('bda.txt', 'a+') as file2:
    file2.write('outra linha\n')
    file2.seek(0)
    print(file2.read())
