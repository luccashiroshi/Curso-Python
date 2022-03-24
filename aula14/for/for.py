"""
For em python
iterando strings com for
função range(start=0, stop, step=1)
"""
texto = 'Python'

c = 0

for letra in texto:
    print(letra)

print("-----------------------------------")


for n in range(5, 10, 2):
    print(n)

print("-----------------------------------")

for n in range(100):
    if n % 9 == 0:
        print(n)

        