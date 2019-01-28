class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

def najstarszy(*args):
    dog_ages = []
    for dog in args:
        dog_ages.append([dog.age, dog])
    dog_ages.sort()
    return dog_ages[-1][1]

azor = Dog("Azor", 2)
rex = Dog("Rex", 5)
mruczek = Dog("Mruczek", 10)

dog = najstarszy(azor, rex, mruczek)
print(dog.name)