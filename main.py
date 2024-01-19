#-----------------------------задача-------------------------------------------
# реализовать класс
# Класс SantaClaus
# Атрибуты: имя, возраст, количество подарков.
# Методы: give_gifts(), update_age().
# НЕОБЯЗАТЕЛЬНО: Интерфейс для отправки подарков и обновления возраста.

class SantaClaus:
    def __init__(self, name, age, quantity_gifts):
        self.name = name
        self.age = age
        self.quantity_gifts = quantity_gifts

    def getName(self):
        return self._name

    def update_age(self):
        return self._age

    def quantity_gifts(self):
        return self._quantity_gifts

Claus = SantaClaus("Kerstmann", "1754", "10000")
print(Claus.name)
print(Claus.age)
print(Claus.quantity_gifts)









