import unittest

from poker.card import Card

from poker.validator import RoyalFlushValidator


class RoyalFlushValidatorTest(unittest.TestCase):
    def test_validates_that_card_do_not_have_a_straight_flush_ending_with_an_ace(self):
        cards = [
            Card(rank = "9", suit = "Clubs"),
            Card(rank = "10", suit = "Clubs"),
            Card(rank = "Jack", suit = "Clubs"),
            Card(rank = "Queen", suit = "Clubs"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Diamonds"),
        ]

        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_validates_that_card_do_have_a_straight_flush_ending_with_an_ace(self):
        cards = [
            Card(rank = "2", suit = "Spades"),
            Card(rank = "10", suit = "Clubs"),
            Card(rank = "Jack", suit = "Clubs"),
            Card(rank = "Queen", suit = "Clubs"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Clubs"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_retruns_five_striaght_cards__ending_with_an_ace(self):
        ten = Card(rank = "10", suit = "Clubs")
        jack =  Card(rank = "Jack", suit = "Clubs")
        queen = Card(rank = "Queen", suit = "Clubs")
        king = Card(rank = "King", suit = "Clubs")
        ace = Card(rank = "Ace", suit = "Clubs")
        
        
        cards = [
            Card(rank = "2", suit = "Spades"),
            ten,
            jack,
            queen,
            king,
            ace,
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                ten, 
                jack,
                queen,
                king,
                ace
            ]
        )

   
