"""


"""

import pytest
import random
from random import randint


class Przedmiot:
    def __init__(self, nazwa, bonus):
        """

        :param nazwa: string
        :param bonus: int
        """
        self.nazwa = nazwa
        if isinstance(bonus, int):
            self.bonus_do_ataku = bonus
        else:
            raise ValueError("Bonus powinien być liczbą")

    def __str__(self):
        return f"{self.nazwa}, {self.bonus_do_ataku} do ataku\n"


class Postac:

    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self._atak = atak
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.ekwipunek = []

    @property
    def atak(self):
        bonusy = 0
        for przedmiot in self.ekwipunek:
            bonusy += przedmiot.bonus_do_ataku
        # bonusy = sum([e.bonus_do_ataku for e in self.ekwipunek])
        return self._atak + bonusy

    def otrzymaj_obrazenia(self, obrazenia):
        print(f"{self.imie} oberwał za {obrazenia} obrażeń.")
        self.zdrowie -= obrazenia
        if self.zdrowie < 0:
            self.zdrowie = 0

    def wylecz(self, pkt_zdrowia):
        if self.zdrowie == 0:
            return False
        self.zdrowie += pkt_zdrowia
        if self.zdrowie > self.max_zdrowie:
            self.zdrowie = self.max_zdrowie

    def dodaj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def __str__(self):
        napis = f"""
Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia.
EKWPIUNEK:       
"""
        for przedmiot in self.ekwipunek:
            # napis += f"{przedmiot.nazwa}, {przedmiot.bonus_do_ataku} do ataku\n"
            napis += str(przedmiot)
        return napis

    def zabierz_przedmiot(self, przedmiot):
        self.ekwipunek.remove(przedmiot)

    def moc_ataku(self):
        return random.randint(self.atak // 2, self.atak)

    @staticmethod
    def walka(atakujcy, broniacy):

        print(f"Walka {atakujcy.imie} vs {broniacy.imie}")
        print(atakujcy)
        print(broniacy)
        print("-" * 40)

        while atakujcy.zdrowie > 0 and broniacy.zdrowie > 0:
            moc_ataku_atakujacego = atakujcy.moc_ataku()
            print(f"{atakujcy.imie} uderza {broniacy.imie} z mocą {moc_ataku_atakujacego}")
            broniacy.otrzymaj_obrazenia(moc_ataku_atakujacego)

            print("-" * 20)

            if broniacy.zdrowie > 0:
                moc_ataku_broniacego = broniacy.moc_ataku()
                print(f"{broniacy.imie} uderza {atakujcy.imie} z mocą {moc_ataku_broniacego}")
                atakujcy.otrzymaj_obrazenia(moc_ataku_broniacego)

        print("KONIEC Walki")

        print(atakujcy)
        print(broniacy)


class Polozenie():

    def __init__(self, x, y, zasieg_x, zasieg_y):
        self.x = x
        self.y = y
        self.zasieg_x = zasieg_x
        self.zasieg_y = zasieg_y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def w(self):
        self.y += 1
        if self.y > self.zasieg_y:
            print("Wyszedłeś poza planszę")
            exit()

    def s(self):
        self.y -= 1
        if self.y < 1:
            print("Wyszedłeś poza planszę")
            exit()

    def a(self):
        self.x -= 1
        if self.x < 1:
            print("Wyszedłeś poza planszę")
            exit()

    def d(self):
        self.x += 1
        if self.x > self.zasieg_x:
            print("Wyszedłeś poza planszę")
            exit()

    def __str__(self):
        return f"Położenie: x = {self.x}, y = {self.y}"


class Plansza:

    def __init__(self, gracz, wrog, skarb, x=10, y=10):
        self.gracz = gracz
        self.wrog = wrog
        self.skarb = skarb
        self.x = x
        self.y = y

        self.polozenie_gracza = Polozenie(randint(1, self.x), randint(1, self.y), self.x, self.y)
        self.polozenie_wroga = Polozenie(randint(1, self.x), randint(1, self.y), self.x, self.y)
        self.polozenie_skarbu = Polozenie(randint(1, self.x), randint(1, self.y), self.x, self.y)

    def ruch(self):
        print("Gracz: ", self.polozenie_gracza)
        print("Wróg: ", self.polozenie_wroga)
        print("Skarb: ", self.polozenie_skarbu)

        kierunek = input("Podaj kierunek w-góra, s-dół, a-lewo,d-prawo: ")
        getattr(self.polozenie_gracza, kierunek)()


        if self.polozenie_gracza == self.polozenie_skarbu:
            print("Otrzymałes: ", self.skarb)
            self.gracz.dodaj_przedmiot(self.skarb)
            self.skarb = None
            self.polozenie_skarbu = Polozenie(None, None, self.x, self.y)

        if self.polozenie_gracza == self.polozenie_wroga:
            Postac.walka(self.gracz, self.wrog)
            if self.gracz.zdrowie < 1:
                print("Zginąłeś...")
                exit()
            else:
                print("Twoja przygotwa trwa...")

    def gra(self):
        while True:
            self.ruch()


# polozenie_gracza = Polozenie(1, 1, 10, 10)
# polozenie_skarbu = Polozenie(2, 2, 10, 10)
#
# while True:
#     print(polozenie_gracza)
#     kierunek = input("Podaj kierunek w-góra, s-dół, a-lewo,d-prawo: ")
#     getattr(polozenie_gracza, kierunek)()


kruger = Postac("Fredie Kruger", 40, 200)
kula = Przedmiot("Kula", 5)
noz = Przedmiot("Noz", 5)
kruger.dodaj_przedmiot(kula)
kruger.dodaj_przedmiot(noz)

rufus = Postac("Rufus", 30, 100)
janusz = Postac("Janusz", 40, 120)

tulipan = Przedmiot("Zielony tuplian zniszczenia", 5)
rufus.dodaj_przedmiot(tulipan)

plansza = Plansza(rufus, janusz, noz)
plansza.gra()


#
# Postac.walka(rufus, janusz)
#
# kierunek = input("Podaj kierunek w-góra, s-dół, a-lewo,d-prawo: ")
# if kierunek == "w":
#     gracz_y1 += 1
# elif kierunek == "s":
#     gracz_y1 -= 1
# elif kierunek == 'a':
#     gracz_x1 -= 1
# elif kierunek == 'd':
#     gracz_x1 += 1
#
#


def test_nowa_postac():
    postac = Postac("Albert", 1, 20)
    assert postac.imie == "Albert"
    assert postac.atak == 1
    assert postac.zdrowie == 20
    assert postac.max_zdrowie == 20


def test_obrazenia():
    postac = Postac("Rafał", 5, 200)
    assert postac.zdrowie == 200
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.otrzymaj_obrazenia(200)
    assert postac.zdrowie == 0


def test_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(50)
    assert postac.zdrowie == 170


def test_leczenie_nieboszczyka():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(800)
    assert postac.zdrowie == 0
    postac.wylecz(50)
    assert postac.zdrowie == 0


def test_za_duze_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(500)
    assert postac.zdrowie == 200


def test_postac_dodaj_przedmiot():
    postac = Postac("Rafał", 5, 200)
    przedmiot = Przedmiot("Rękawice grzmoty", 40)
    assert przedmiot not in postac.ekwipunek
    assert postac.atak == 5
    postac.dodaj_przedmiot(przedmiot)
    assert postac.atak == 45
    assert przedmiot in postac.ekwipunek


def test_postac_zabierz_przedmiot():
    postac = Postac("Rafał", 5, 200)
    przedmiot = Przedmiot("Rękawice grzmoty", 40)
    assert przedmiot not in postac.ekwipunek
    assert postac.atak == 5
    postac.dodaj_przedmiot(przedmiot)
    assert postac.atak == 45
    assert przedmiot in postac.ekwipunek
    postac.zabierz_przedmiot(przedmiot)
    assert przedmiot not in postac.ekwipunek
    assert postac.atak == 5


def test_przedmiot():
    przedmiot = Przedmiot("Kula mocy", 10)
    assert przedmiot.nazwa == "Kula mocy"
    assert przedmiot.bonus_do_ataku == 10


def test_przedmiot_bonus_is_not_int():
    with pytest.raises(ValueError):
        Przedmiot("Kula mocy", "dziesięć")


def test_postac_moc_ataku():
    postac = Postac("Rafał", 50, 200)
    assert postac.atak == 50
    moc_atak = postac.moc_ataku()
    assert (postac.atak // 2) <= moc_atak <= postac.atak