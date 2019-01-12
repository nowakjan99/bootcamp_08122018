print([x/10 for x in range(11)])

print({(x, x**2, x**3) for x in range(-10,11)})

napisy = {"Ala ma kota", "kot ma alę", "Zażółć gęślą jaźń"}
print({x: len(x) for x in napisy})