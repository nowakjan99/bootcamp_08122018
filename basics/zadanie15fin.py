from random import randint

gracz_x = randint(1, 10)
gracz_y = randint(1, 10)
skarb_x = randint(1, 10)
skarb_y = randint(1, 10)

min_l_krokow_po_wyl = abs(skarb_x-gracz_x) + abs(skarb_y-gracz_y)
liczba_krokow = 0

DEBUG = False

while True:
    min_l_krokow_przed_ruchem = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    print(f"Twoja pozycja to: {gracz_x}, {gracz_y}")

    if DEBUG:
        print("DEBUG info:")
        print(f"Pozycja skarbu to: {skarb_x}, {skarb_y}")
        print("Minimalna liczba krokow", min_l_krokow_po_wyl)

    kierunek = input("Podaj kierunek w-góra, s-dół, a-lewo,d-prawo: ")
    if kierunek == "w":
        gracz_y += 1
    elif kierunek == "s":
        gracz_y -= 1
    elif kierunek == 'a':
        gracz_x -= 1
    elif kierunek == 'd':
        gracz_x += 1

    liczba_krokow += 1
    min_l_krokow_po_ruchu = abs(skarb_x-gracz_x) + abs(skarb_y-gracz_y)

    if gracz_x < 1 or gracz_y < 1 or gracz_x > 10 or gracz_y > 10:
        print("Wyszedłeś poza planszę. Koniec gry")
        break

    if gracz_x == skarb_x and gracz_y == skarb_y:
        print("Wygrałeś!!")
        print(f"Minimalna liczba kroków wynosiła: {min_l_krokow_po_wyl}")
        print(f"Zrobiłeś kroków: {liczba_krokow}")
        break

    los = randint(1, 5)
    if los != 3:
        if min_l_krokow_po_ruchu < min_l_krokow_przed_ruchem:
            print("Ciepło")
        else:
            print("Zimno")

    if liczba_krokow >= min_l_krokow_po_wyl * 2:
        skarb_x = randint(1, 10)
        skarb_y = randint(1, 10)
        min_l_krokow_po_wyl = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
        liczba_krokow = 0
        print("Przekroczyłeś dopuszczalną liczbę kroków. Skarb zmienił położenie")