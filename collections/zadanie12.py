liczby = [9, 2, 6, 8, 4, 3, 1, 0]
66
for i in range(len(liczby)):
    in indeks_minimum = i
    for j in range(i,(liczby)):
        if liczby[j] < liczby[indeks_minimum]:
            indeks_minimum = j
    liczby[i], liczby[indeks_minimum] = liczby[indeks_minimum], liczby[i]


print(liczby)





# assert == [0, 1, 2, 3, 4, 6, 8, 9]