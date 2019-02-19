import requests
import decimal

resp = requests.get("http://api.nbp.pl/api/exchangerates/tables/A?format=json")
kursy = resp.json(parse_float=decimal.Decimal)[0]['rates']

print("Dysponuję walutami")
for k in kursy:
    print(k)

waluta = input("Podja kod waluty którą chcesz kupić: ")
za_ile = decimal.Decimal(input("Za ile PLN chcesz kupić? "))

for k in kursy:
    if k['code'] == waluta:
        print(f"Za {za_ile} PLN możesz kupić {za_ile/k['mid']:.2f} {waluta}")
