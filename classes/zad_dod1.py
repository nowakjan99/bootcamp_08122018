from collections import OrderedDict

dict_val = OrderedDict([
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1)
])


# konwerter = Konwerter()


class Konwerter(object):
    dict_val = {'M': 1000,
                'CM': 900,
                'D': 500,
                'CD': 400,
                'C': 100,
                'XC': 90,
                'L': 50,
                'XL': 40,
                'X': 10,
                'IX': 9,
                'V': 5,
                'IV': 4,
                'I': 1}

    def fahr_to_cel(self, val):
        cel = (val - 32) * 5 / 9
        return cel

    @staticmethod
    def cel_to_fahr(val):
        fahr = val * 9 / 5 + 32
        return fahr

    @classmethod
    def int_to_roman(cls, num):
        if not (0 < num <= 3999):
            return "Liczba poza przedziałem"
        elif isinstance(num, int):
            result = ''
            for k, v in cls.dict_val.items():
                while num >= v:
                    result += k
                    num -= v
            return result

    # "XIV"
    @staticmethod
    def roman_to_int(rom):
        result = 0
        for i in range(len(rom)):
            if i > 0 and Konwerter.dict_val[rom[i]] > Konwerter.dict_val[rom[i - 1]]:
                         # V   5                          I   2 * 1
                result += Konwerter.dict_val[rom[i]] - 2 * Konwerter.dict_val[rom[i - 1]]
            else:
                # X 10, I -> 10+1,
                result += Konwerter.dict_val[rom[i]]
        return result


assert Konwerter().fahr_to_cel(32) == 0
assert Konwerter.cel_to_fahr(0) == 32

print(Konwerter.int_to_roman(4))