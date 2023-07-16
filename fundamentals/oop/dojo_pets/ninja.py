# For this assignment, you'll be asked to create a Ninja class and a Pet class. Your Ninjas will be able to have a pet - and you can even practice using inheritance by creating sub-classes of pets, if you're ready to stretch yourself!

# Create a Ninja class with the ninja attributes listed above.
# Implement walk(), feed(), bathe() on the ninja class.
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()


