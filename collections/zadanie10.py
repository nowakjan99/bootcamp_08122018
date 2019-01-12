# text = input("Podaj napis: ")

znaki = {

}

text = "Ala ma kota"

for znak in text:
    # if znak in znaki:
    #     znaki[znak] += 1
    # else:
    #     znaki[znak] = 1
    znaki[znak] = znaki.get(znak, 0) + 1

print("Statystyka: ")
for z, c in znaki.items():
    print(f' - {z} wystąpił {c} razy')