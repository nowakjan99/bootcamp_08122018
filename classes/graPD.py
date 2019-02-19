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
        return random.randint(self.atak//2, self.atak)

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

gracz_x1 = randint(1, 10)
gracz_y1 = randint(1, 10)
gracz_x2 = randint(1, 10)
gracz_y2 = randint(1, 10)

przedmiot_x1 = randint(1, 10)
przedmiot_y1 = randint(1, 10)
przedmiot_x2 = randint(1, 10)
przedmiot_y2 = randint(1, 10)

rufus = Postac("Rufus", 30, 100)
kruger = Postac("Fredie Kruger", 25, 110)
kula = Przedmiot("Kula", 7)
noz = Przedmiot("Noz", 5)

while True:

    print(f"Twoja pozycja to: {gracz_x1}, {gracz_y1}")
    print(f"pozycja przeciwnika to: {gracz_x2}, {gracz_y2}")
    print(f"pozycja skarbu1 to: {przedmiot_x1}, {przedmiot_y1}")
    print(f"pozycja skarbu2 to: {przedmiot_x2}, {przedmiot_y2}")

    if gracz_x1 == gracz_x2 and gracz_y1 == gracz_y2:
        print(f"Natrafiasz na Rufusa.")
        Postac.walka(rufus, kruger)
        break

    kierunek = input("Podaj kierunek w-góra, s-dół, a-lewo,d-prawo: ")
    if kierunek == "w":
        gracz_y1 += 1
    elif kierunek == "s":
        gracz_y1 -= 1
    elif kierunek == 'a':
        gracz_x1 -= 1
    elif kierunek == 'd':
        gracz_x1 += 1

    if gracz_x1 < 1 or gracz_y1 < 1 or gracz_x1 > 10 or gracz_y1 > 10:
        print("Wyszedłeś poza planszę. Koniec gry")
        break

    if gracz_x1 == przedmiot_x1 and gracz_y1 == przedmiot_y1:
        print(f"Zdobywasz {kula}!!")
        kruger.dodaj_przedmiot(kula)
        przedmiot_x1 = 0
        przedmiot_y1 = 0
        continue

    if gracz_x2 == przedmiot_x1 and gracz_y2 == przedmiot_y1:
        print(f"Rufus zdobywa {kula}!!")
        rufus.dodaj_przedmiot(kula)
        przedmiot_x1 = 0
        przedmiot_y1 = 0
        continue

    if gracz_x1 == przedmiot_x2 and gracz_y1 == przedmiot_y2:
        print(f"Zdobywasz {noz}!!")
        kruger.dodaj_przedmiot(noz)
        przedmiot_x2 = 0
        przedmiot_y2 = 0
        continue

    if gracz_x2 == przedmiot_x2 and gracz_y2 == przedmiot_y2:
        print(f"Rufus zdobywa {noz}!!")
        rufus.dodaj_przedmiot(noz)
        przedmiot_x2 = 0
        przedmiot_y2 = 0
        continue

    ruch_gracz2 = randint(1, 4)

    if ruch_gracz2 == 1 and gracz_y2 < 10:
        gracz_y2 += 1
    if ruch_gracz2 == 1 and gracz_y2 == 10:
        gracz_y2 -= 1
    if ruch_gracz2 == 2 and gracz_y2 > 1:
        gracz_y2 -= 1
    if ruch_gracz2 == 2 and gracz_y2 == 1:
        gracz_y2 += 1
    if ruch_gracz2 == 3 and gracz_x2 > 1:
        gracz_x2 -= 1
    if ruch_gracz2 == 3 and gracz_x2 == 1:
        gracz_x2 += 1
    if ruch_gracz2 == 4 and gracz_x2 < 10:
        gracz_x2 += 1
    if ruch_gracz2 == 4 and gracz_x2 == 10:
        gracz_x2 -= 1
















