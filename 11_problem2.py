from unicodedata import name


class Animal:
    Animalname = "Rocky"

class Pet(Animal):
    color = "Black"

class Dog(Pet):

    @staticmethod
    def bark():
        print("Bow Bow!")

d = Dog()
d.bark()
