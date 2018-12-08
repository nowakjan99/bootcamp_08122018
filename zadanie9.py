rok_uro = int(input("Podaj swój rok urodzenia: "))

import datetime

year = datetime.datetime.now().year

if year - rok_uro >= 18:
    print("Jesteś pełnoletni")
else:
    print("Nie jesteś pełnoletni")