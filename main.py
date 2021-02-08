from poker.card import Card 
from poker.deck import Deck
from poker.hand import Hand
from poker.player import Player

deck = Deck()
cards = Card.create_standard_52_cards()

deck.add_cards(cards)

hand1 = Hand(cards = [])
hand2 = Hand(cards = [])

player1 = Player(name = "Ismail", hand = hand1)
player2 = Player(name = "Munira", hand = hand2)



#from main import deck, cards, hand1, hand2, player1, player2