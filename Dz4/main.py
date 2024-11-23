class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        return "Голос"

    def info(self):
        return f"Животное: {self.name}, Возвраст: {self.age} лет"

class Dog(Animal):
    def sound(self):
        return "Гав-гав!"

    def fetch_ball(self):
        return f"{self.name} принес мячик!"


# Subclass Cat
class Cat(Animal):
    def sound(self):
        return "Мяу"

    def climb_tree(self):
        return f"{self.name} залез на дерево!"


barni = Dog("Барни", 4)
bonya = Cat("Боня", 3)

print(barni.info())
print(barni.sound())
print(barni.fetch_ball())

print(bonya.info())
print(bonya.sound())
print(bonya.climb_tree())
