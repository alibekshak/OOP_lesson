 # Наследование - Inheritance
from datetime import datetime
class Vehicla():
    def __init__(self, name, engine, created):

        self.name = name
        self.engine = engine
        self.created = created

    def get_name(self):
        return self.name

    def get_created(self):
        self.created = datetime.now().strftime("%Y.%m.%d")
        return  self.created

class Car(Vehicla):
    def __init__(self, name, engine, created, whell):
        super().__init__(name, engine, created)

        self.wheel = whell

    def __str__(self):
        return f"{self.name}, {self.engine}, {self.created}, {self.wheel}"

car1 = Car("BMW", "V6", '2022', '4')
car1.get_created()
print(car1)
print(car1.__dict__)

#____________________________________________________________________________________________

class Lists:
    def generate_number(self):
        numbers = [i for i in range(20)]
        return numbers


class Output_l(Lists):
    def __init__(self, chet, nchet) -> list:

        self.chet = chet
        self.nchet = nchet
        self.numbers = self.generate_number()

    def chec(self):
        for i in self.numbers:
            if i % 2 == 0:
                self.chet.append(i)
            else:
                self.nchet.append(i)
        return self.chet, self.nchet


n = Output_l([], [])

print(n.chec())
