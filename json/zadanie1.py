import json
import getpass

try:
    with open("employees.json") as fp:
        pracownicy = json.load(fp)
except FileNotFoundError:
    pracownicy = []


def dodaj_pracownika(pracownicy):
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    rok_urodzenia = input("Podaj rok urodzenia: ")
    pensja = input("Pensja: ")

    pracownik = {
        "imie": imie,
        "nazwisko": nazwisko,
        "rok_urodzenia": rok_urodzenia,
        "pensja": pensja
    }

    pracownicy.append(pracownik)

    with open("employees.json", 'w') as fp:
        json.dump(pracownicy, fp)


def wypisz_pracownikow(pracownicy):
    print("Pracownicy: ")
    for nr, pracownik in enumerate(pracownicy, start=1):
        print(
            f"- [{nr}] {pracownik['imie']} {pracownik['nazwisko']} - rok: {pracownik['rok_urodzenia']}, "
            f"pensja: {pracownik['pensja']} PLN ")


def usun_pracownika(pracownicy):
    nr = input("Którego pracownika usunąć? ")
    haslo = getpass.getpass("Podaj hasło! ")
    if haslo != 'TAJNE':
        print("Złe hasło")
        return
    del pracownicy[int(nr) - 1]

    with open("employees.json", 'w') as fp: json.dump(pracownicy, fp)


wybor = input("Co chcesz zrobic? [d - dodaj, w - wypisz]: ")

if wybor == "d":
    dodaj_pracownika(pracownicy)
elif wybor == "w":
    wypisz_pracownikow(pracownicy)
elif wybor == "u":
    wypisz_pracownikow(pracownicy)
    usun_pracownika(pracownicy)