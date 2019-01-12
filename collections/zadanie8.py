tekst = input("Podaj tekst: ")

#tekst1 = "Ala ma kota"
#tekst2 = "Ala <ma> kota"
#tekst3 = "Ala <>ma kota"

dlugosc = 0
licz = False

for znak in tekst:
    if znak == "<":
        licz = True
    elif znak == ">":
        licz = False
        break
    elif licz:
        dlugosc += 1

print(f"Liczba znakow pomiedzy <> wynosi {dlugosc}")


