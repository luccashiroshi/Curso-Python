from datetime import datetime, timedelta

date = datetime(2022, 2, 9, 10, 40, 59)
print(date.strftime('%d/%m/%Y %H:%M:%S'))

data = datetime.strptime('20/02/2018', '%d/%m/%Y')
print(data)

print(data.timestamp())

print(f'a data fromtimestamp = {datetime.fromtimestamp(1519095600.0)}')

print(data.strftime('%d/%m/%Y %H:%M:%S'))
data = data + timedelta(days=8, seconds=45)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

d1 = datetime.strptime('21/04/2020', '%d/%m/%Y')
d2 = datetime.strptime('14/12/2021', '%d/%m/%Y')
dif = d2 - d1
print(dif)
print(dif.total_seconds())
