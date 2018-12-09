# x = int(input("Podaj temperaturę w poniedzialek: "))
# y = int(input("Podaj temperaturę we wtorek: "))
# z = int(input("Podaj temperaturę w srode: "))
# a = int(input("Podaj temperaturę w czwartek: "))
# b = int(input("Podaj temperaturę w piatek: "))
# c = int(input("Podaj temperaturę w sobote: "))
# d = int(input("Podaj temperaturę w niedziele: "))
#
# dzien = 1
#
# while dzien < 8:
#     wynik = (x + y + z + a + b + c + d) / 7
#     print("Srednia temperatura w tygodniu: ", wynik)
#     break


ILE_DNI = 7

temp = 0
i = 1
while i <= ILE_DNI:
        komenda = input(f"Podaj temperature w dniu {i} lub [k] by zakończyć: ")
        if komenda == 'k':
            break
        temp_i = float(komenda)
        temp += temp_i
        i += 1
print("Średnia temperatura wynosiła: ", temp/(i-1))