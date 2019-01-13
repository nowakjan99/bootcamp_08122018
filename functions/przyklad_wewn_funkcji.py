
def loguj_uzycie(func):
    """To będzie dekorator. Wypisze tekst przed i po uruchomieniu"""

    def wrapper():
        print("To się wykona przed")
        func()
        print("To się wykona po")

    return wrapper

def pobierz_dane():
    print("Pobrałem dane")

print("nie udekorowane")
pobierz_dane()

print("udekorowane")
pobierz_dane = loguj_uzycie(pobierz_dane)
pobierz_dane()