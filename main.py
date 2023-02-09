class Planet:
    def __init__(self, name, square, speed):
        self.name = name
        self.square = square
        self.speed_of_light = speed


class Age(Planet):
    def __init__(self, name, square, speed_of_light):
        super().__init__(name, square, speed_of_light)

    def age(self):
        return f"Возраст планеты {self.square * self.speed_of_light} миллиардов лет, название планеты {self.name}"


class Satellite(Planet):
    def __init__(self, name, satel):
        self.satel = satel
        self.name = name

    def satell(self):
        return f"Спутник {self.name} - {self.satel}"

class Earth(Planet):
    def __init__(self, name, square, speed_of_light):
        super().__init__(name, square, speed_of_light)

    def life(self):
        return f"{self.name} обитаемая планета"


class Jupiter(Planet):
    def __init__(self, name, square, speed_of_light):
        super().__init__(name, square, speed_of_light)

    def life(self):
        return f"{self.name} необитаемая планета"


class Venus(Planet):
    def __init__(self, name, square, speed_of_light):
        super().__init__(name, square, speed_of_light)

    def life(self):
        return f"{self.name} необитаемая планета"


live = [Earth("Earth", 4, 1.08), Jupiter("Jupiter", 4.3, 1.08), Venus("Venus", 4, 1.08)]
for i in live:
    print(i.life())

print("_"*30)

satell1 = Satellite("Earth", "Moon")
satell2 = Satellite("Jupiter", "Europa and other 91")
satell3 = Satellite("Venus", "No moons")

planets = [Age("Earth", 4, 1.08), Age("Jupiter", 4.3, 1.08), Age("Venus", 4, 1.08)]
for i in planets:
    print(i.age())
    print(i.__dict__)

print("_"*30)

print(satell1.satell())
print(satell2.satell())
print(satell3.satell())