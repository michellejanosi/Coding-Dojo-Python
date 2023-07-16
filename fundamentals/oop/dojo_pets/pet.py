# Create a Pet class with the pet attributes listed above.
# Implement sleep(), eat(), play(), noise() methods on the pet class.
class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5

    def noise(self):
        print(f'{self.name} makes a noise!')

# SENSEI BONUS: Use Inheritance to create sub classes of pets.
class Dog(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, "Dog", tricks)

    def noise(self):
        print(f'{self.name} barks!')
