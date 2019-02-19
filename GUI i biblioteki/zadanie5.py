import re
import json

with open("input.txt") as f:
    input = f.read()

print("kody pocztowe: ", re.findall(r'\d\d-\d\d\d', input))
print("adresy e-mail: ", re.findall(r'[\w\-+.]+@[\w\-.]{4,}', input))
print("daty: ", re.findall(r'\b\d{1,2}\s[A-Z][a-z]{2}\s\d{4}\b', input))

print()
print("dlugie sekwencje liczb zawierajace kod pocztowy: ", re.findall(r'\D(\d\d-\d\d\d)\D', input))

