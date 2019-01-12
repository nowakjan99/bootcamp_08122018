def wiecej_niz(napis, prog):
    wynik = set()
    unikalne = set(napis)
    for c in unikalne:
        if napis.count(c) > prog:
            wynik.add(c)

    return wynik

def test_wiecej_niz():
    assert wiecej_niz('ala ma kota a kot ma ale', 3) == {"a", " "}