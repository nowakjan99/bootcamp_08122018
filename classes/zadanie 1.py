class Product:

    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f'Produkt {self.nazwa}, id: {self.id}, cena {self.cena} PLN')



produkt = Product(1, "Woda", 2.99)
produkt.print_info()
