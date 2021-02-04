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

    def test_figure_out_pair_is_best_rank(self):
        cards = [
            Card(rank= "Ace", suit= "Spades"),
            Card(rank= "Ace", suit= "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Pair"
        )
    def test_figure_out_two_pair_is_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "5", suit = "Clubs"),
            Card(rank = "Ace", suit = "Clubs"),
            Card(rank = "King", suit = "Hearts"),
            Card(rank = "King", suit = "Diamonds")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Two Pair"
        )
    
    def test_figure_out_three_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "King", suit = "Hearts"),
            Card(rank = "King", suit = "Diamonds"),
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "5", suit = "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Three of a Kind"
        )
    
    