# lista[10, 20, 30 , 40]
#
# def rekuprint(lista):
#     if len(lista) == 1:
#         print(lista[0])
#     else:
#         print(lista[0])
#         rekuprint(lista[1:0])
#
# rekuprint(lista)

def powieksz_o_jeden(liczba):
    liczba += 1
    print(liczba)
    powieksz_o_jeden(liczba)
powieksz_o_jeden(1)