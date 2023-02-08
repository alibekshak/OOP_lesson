#Полиморфизм

class Animal:

    def speak(self):
        return "Something"

class Dog(Animal):
    def speak(self):
        return "Gav gav"

class Cat(Animal):
    def speak(self):
        return "Miyau miyau"

class Chickin(Animal):
    def speak(self):
        return "Ko ko ko"

class Ant(Animal):

    def a(self):
        return "I'm ant"

animals = [Dog(), Cat(), Chickin(), Ant()]
for i in animals:
    print(i.speak())

ant1 = Ant()
print(ant1.a())


