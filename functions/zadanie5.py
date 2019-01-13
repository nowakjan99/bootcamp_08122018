import pytest

def silnia(param):
    if param < 0:
        raise ValueError("Argument musi być >= 0")
    if param == 0:
        return 1
    else:
        return param * silnia(param-1)



def test_silnia_dla_0():
    assert silnia(0) == 1

def test_silnia_dla_wieksze_od_0():
    assert silnia(5) == 120

def test_silnia_dla_mniejsze_od_0():
    with pytest.raises(ValueError) as e:
        silnia(-10)