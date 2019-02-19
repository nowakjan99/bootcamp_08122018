import re

s = "Ala ma kota! kot ma Ale. Kot lubi mleko. Nie lubi ryb."

print(re.findall('lubi', s))
print(re.findall('lubi .', s))
print(re.findall('.{2} ma', s))
print(re.findall(r'\w* ma', s))
print(re.findall(r'\w+', s))
print(re.findall(r'[A-Z]', s))
print(re.findall(r'[A-Z].*\.', s))
print(re.findall(r'[A-Z].*?\.', s))
print(re.findall(r'[A-Z].*?[\.\!]', s))
print(re.findall(r'[A-Z]\w*\s.*?[\.\!]', s))
print(re.findall(r'[A-Z]\w*\W.*?[\.\!]', s))
print(re.findall(r'([A-Z]\w*)\W.*?[\.\!]', s))

# powinno być r przed '\'

