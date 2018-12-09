from random import randint


x = randint(1,10)
y = randint(1,10)
a = randint(1,10)
b = randint(1,10)


print(f"Twoje położenie:  [{x},{y}]")
while True:

    min_kroki = abs(a - x) + abs(b - y)
    print("minimalna liczba kroków wynosi:", min_kroki)

    ruchX = int(input("Jaki wykonujesz ruch po x?(jeśli ruszasz się w lewo użyj znaku '-'" ))
    ruchY = int(input("Jaki wykonujesz ruch po y?(jesli ruszasz się w dół użyj znaku '-'" ))
    if x < 0 or y < 0:
        print("Przegrałeś)")
    elif ruchX > 1 or ruchY > 1:
        print("Niezdowolony ruch")
    else:
        x += ruchX
        y += ruchY
        print(f"Twoje położenie:  [{x},{y}]")
    if x == a and y == b:
        print("Wygrales")
        break

