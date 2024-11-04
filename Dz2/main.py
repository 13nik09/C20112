class Dog:
    def __init__(self, name):
        self.name = name
        self.energy = 50
        self.hunger = 50
        self.happiness = 0

        print(f"{self.name} прокинувся. Голод: {self.hunger}, Енергія: {self.energy}, Щастя: {self.happiness}")
        print("    ")

    def eat(self):
        self.hunger -= 50
        self.energy += 20
        self.happiness += 10
        print(f"{self.name} їсть. Голод: {self.hunger}, Енергія: {self.energy}, Щастя: {self.happiness}")

    def sleep(self):
        self.energy += 30
        self.hunger += 10
        self.happiness += 20
        print(f"{self.name} заснув. Голод: {self.hunger}, Енергія: {self.energy}, Щастя: {self.happiness}")

    def eat2(self):
        self.hunger -= 10
        self.happiness += 10
        print(f"{self.name} перекусує. Голод: {self.hunger}, Енергія: {self.energy}, Щастя: {self.happiness}")

    def play(self):
        self.happiness += 60
        self.energy -= 20
        self.hunger += 30
        print(f"{self.name} грається. Голод: {self.hunger}, Енергія: {self.energy}, Щастя: {self.happiness}")

barni = Dog("Барні")

barni.eat()
barni.sleep()
barni.eat2()
barni.play()

