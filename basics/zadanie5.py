Miasto_A = input("Miasto A: ")
Miasto_B = input("Miasto B: ")
Dystans = int(input(f"Dystans {Miasto_A} - {Miasto_B}: "))
Cena_paliwa = float(input("Cena paliwa: "))
Spalanie = float(input("Spalanie na 100km: "))

koszt = (Dystans * Spalanie * Cena_paliwa) / 100



print(f"Koszt przejazdu {Miasto_A} - {Miasto_B} to {koszt} PLN")