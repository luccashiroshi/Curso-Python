print('Que horas são?')
hr = input('Horas: ')
min = input('Minutos: ')

try:
    hr = int(hr)
    min = int(min)
    if hr < 12:
        print(f'Bom dia {hr}:{min}')
    elif 12 <= hr <= 17:
        print(f'Boa tarde {hr}:{min}')
    else:
        print(f'Boa noite {hr}:{min}')

except:
    print('ERROR')