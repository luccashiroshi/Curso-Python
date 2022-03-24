
string = '012345678901234567890123456789012345678901234567890123456789'
n = 10
sep1 = [string[i: i+n] for i in range(0, len(string), n)]
retorno = '.'.join(sep1)
print(sep1)
print(retorno)
