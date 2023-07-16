class Game:
    def __init__(self, deck, player):
        self.deck = deck
        self.player = player
        self.current_card = self.deck.draw_card()
        self.card_order = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def start_game(self):
        print("Welcome to Higher or Lower!")
        print("Guess whether the next card will be higher or lower.")

        while len(self.deck.cards) > 0:
            self.current_card.card_info()
            guess = self.player.make_guess()
            next_card = self.deck.draw_card()

            if (self.card_order.index(next_card.string_val) > self.card_order.index(self.current_card.string_val) and guess == "higher") or \
                (self.card_order.index(next_card.string_val) < self.card_order.index(self.current_card.string_val) and guess == "lower"):
                print("You're correct!")
            else:
                print("Sorry, you're wrong.")
                break

            self.current_card = next_card

        print("Game over!")
