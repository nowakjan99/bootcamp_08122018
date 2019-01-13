# liczby = [1, 2, 3, 4]
#
# liczby2 = [5, 6, 7 ,8]

# for i, l in enumerate(liczby):
#     print(f"indeks={i}, wartość={l}")
#
#  for i, l in enumerate(liczby2):
#     print(f"indeks={i}, wartość={l}")

# def drukuj(lista):
#     for i, l in enumerate(lista):
#         print(f'pozycja={i}, wartość={l}')
#
# drukuj(liczby)
# print()
# drukuj(liczby2)


# def wykonaj_operacje(operacja, *args):
#     print(args)
#     return operacja(args)
# print(wykonaj_operacje(min, 10, 20))
#
#
#
# def dodaj(liczba):
#     # Będzie dodawać do siebie wszystkie liczby od 1 do liczba
#     if liczba == 0:
#         return 0
#     else:
#         return liczba + dodaj(liczba-1)
#
# print(dodaj(5))


def sprawdz_czy(x, funkcja1, funkcja2):
    return funkcja1(x) and funkcja2(x)

print(sprawdz_czy(10, lambda x: x<11, lambda x: x%2 == 0))