# NINJA BONUS: Use modules to separate out the classes into different files.
from ninja import Ninja
from pet import Dog

# Create a dog instance from Pet class
dog = Dog('Rex', 'roll over')

# Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.
ninja = Ninja('John', 'Doe', 'bones', 'meat', dog)

# Have the Ninja feed, walk , and bathe their pet.
ninja.feed()
ninja.walk()
ninja.bathe()
