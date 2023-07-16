class Player:
    def make_guess(self):
        while True:
            guess = input("Higher or lower? ")
            if guess.lower() in ["higher", "lower"]:
                return guess.lower()
            else:
                print("Please enter either 'higher' or 'lower'.")
