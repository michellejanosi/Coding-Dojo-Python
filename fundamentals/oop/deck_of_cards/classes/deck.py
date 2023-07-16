from . import card
import random

class Deck:
    def __init__( self ):
        suits = [ '\u2660', '\u2665', '\u2666', '\u2663' ]  # Unicode for spades, hearts, diamonds, and clubs
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def draw_card(self):
        random.shuffle(self.cards)  # Shuffle the deck before drawing a card
        return self.cards.pop()
