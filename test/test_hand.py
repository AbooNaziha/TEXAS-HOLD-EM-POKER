import unittest
from poker.card import Card 
from poker.hand import Hand 

class HandTest(unittest.TestCase):
    def test_receive_and_stores_cards(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "6", suit = "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.cards, 
            cards
        )

    def test_figure_out_high_card_is_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "7", suit = "Clubs")
        ]
        
        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(), 
            "High Card"
        )