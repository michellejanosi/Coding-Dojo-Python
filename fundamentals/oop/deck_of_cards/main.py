# Higher or Lower — Guess whether the next card drawn from the deck will be higher or lower than the current card. If the guess is correct, the player wins, otherwise the player loses, game over.

from classes.deck import Deck
from classes.game import Game
from classes.player import Player

def main():
    player = Player()
    deck = Deck()
    game = Game(deck, player)

    game.start_game()

if __name__ == "__main__":
    main()
