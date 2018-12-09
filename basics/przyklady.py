# # przyklad input
# #
# # x = int(input("Podaj wartość x: "))
# # y = int(input("Podaj wartość y: "))
# #
# #  input zawsze zwraca napis
# #  x = int(x)
# #  y = int(y)
# #
# # print("Suma: ", x + y)
#
# #przyklady wartosci logicznych
#
# x = 2
# y = 5
#
# # print(x > 1 or y > 1)

krotka = (1, 2, 3)
print(type(krotka))
print(krotka)
print(krotka[0])

for el in krotka:
    print(el)

print(krotka.count(1))

krotka2 = ("Napis 1", 'Napis 2', "Napis 1")
print(krotka2.index("Napis 1"))
print(krotka2.count("Napis 1"))
