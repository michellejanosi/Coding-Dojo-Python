# Attributes:
# On instantiation of a user, the following attributes should be passed in as arguments:

# first_name
# last_name
# email
# age
# Also include default attributes:

# is_rewards_member - default value of False
# gold_card_points = 0

# Methods:
# display_info(self) - Have this method print all of the users' details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.

# Ninja Bonuses:

# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
# Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        # Have this method print all of the users' details on separate lines.
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Rewards member:", self.is_rewards_member)
        print("Gold card points:", self.gold_card_points)

    def enroll(self):
        # Have this method change the user's member status to True and set their gold card points to 200.
        if self.is_rewards_member:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        # have this method decrease the user's points by the amount specified.
        if amount > 0 and amount <= self.gold_card_points:
            self.gold_card_points -= amount
            print(f"Successfully used {amount} points. New balance: {self.gold_card_points} points.")
        else:
            print("The amount must be positive and not exceed the current point balance.")

user1 = User("Sadie", "Smith", "sadie.smith@gmail.com", 29)
user1.display_info()
user1.enroll()
user1.spend_points(100)
