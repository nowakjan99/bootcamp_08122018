# Napisz funkcje, ktora przymie dowolna liczbe napisow,
# 1. zwroci te napisy polaczone znakiem nowej linii
#
# >>> napisy ("a", "b")
# a
# b
#
# >>> napisy ("a", "b", "d")
# a
# b
# d

def napisy(*args, **kwargs):
    return "\n".join(args)



    for k in kwargs:
        tekst = kwargs[k] (tekst)
    return tekst

print("-"*40)
print(napisy("a", "b"))

print("-"*40)
print(napisy("a", "b", "d"))

def upper(napis):
    return napis.upper()

print("-"*40)
print(napisy("a", "b" "c", "d", funkcja=str.upper, funkcja2=str.title))