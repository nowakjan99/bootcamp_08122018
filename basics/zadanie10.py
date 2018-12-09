liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
operacja = input("Podaj rodzaj operacji: ")



# if operacja == "+":
#     print(f"Wynik: {liczba1 + liczba2}")
# else:
#     print("Błąd")
# if operacja == "-":
#     print(f"Wynik: {liczba1 - liczba2}")
# else:
#     print("Błąd")
# if operacja == "*":
#     print(f"Wynik: {liczba1 * liczba2}")
# else:
#     print("Błąd")
# if operacja == "/":
#     print(f"Wynik: {liczba1 / liczba2}")
# else:
#     print("Błąd")

if operacja == "+":
    print(f"Wynik: {liczba1 + liczba2}")
elif operacja == "-":
    print(f"Wynik: {liczba1 - liczba2}")
elif operacja == "/":
    if liczba2 == 0:
        print("Operacja niedozwolona")
    else:
        print(f"Wynik: {liczba1 / liczba2}")
elif operacja == "*":
    print(f"Wynik: {liczba1 * liczba2}")
else:
    print("Operacja nie jest wspierana")
