liczby = [1, 2, 3, 4]

liczby2 = [5, 6, 7 ,8]

# for i, l in enumerate(liczby):
#     print(f"indeks={i}, wartość={l}")
#
#  for i, l in enumerate(liczby2):
#     print(f"indeks={i}, wartość={l}")

def drukuj(lista):
    for i, l in enumerate(lista):
        print(f'pozycja={i}, wartość={l}')

drukuj(liczby)
print()
drukuj(liczby2)
