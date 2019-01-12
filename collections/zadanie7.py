#tekst = input("Podaj tekst: ")

tekst = "Ala ma kota aeiouy"

ile_samoglosek = 0

SAMOGLOSKI = 'aeiouy'

for litera in tekst.lower():
    if litera in SAMOGLOSKI:
        ile_samoglosek += 1


print(ile_samoglosek== 11)