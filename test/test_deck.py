import unittest
from poker.card import Card
from poker.deck import Deck

class DectTest(unittest.TestCase):
    def test_stores_no_card_at_start(self):
        deck = Deck()
        self.assertEqual(
            deck.cards,
            []
        )

    def test_add_cards_to_its_collection(self):
        card = Card(rank = "Ace", suit = "Spades")
        deck = Deck()
        deck.add_cards([card])

        self.assertEqual(
            deck.cards,
            [card]
        )