class Card:
    def __init__( self , suit , string_val ):
        self.suit = suit
        self.string_val = string_val

    def card_info(self):
        print(f"{self.string_val} of {self.suit}")
