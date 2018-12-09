dlugosc = int(input("Podaj długość (cm): "))
szerokosc = int(input("Podaj szerekość (cm): "))
glebokosc = int(input("Podaj głębokość (cm): "))

objetosc = dlugosc * szerokosc * glebokosc

print(objetosc > 1000)


if objetosc > 2000:
    print("Objętość jest większa niż 2 litry")
elif objetosc > 1000:
    print("Objętość jest większa niż 1 litr")
else:
    print("Objętość jest mniejsza niż litr")