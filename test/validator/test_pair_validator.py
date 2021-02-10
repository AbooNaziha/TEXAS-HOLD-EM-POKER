import unittest

from poker.card import Card

from poker.validator import PairValidator

class PairValidatorTest(unittest.TestCase):
    def test_validates_that_card_has_exactly_one_pair(self):
        cards = [
            Card(rank= "Ace", suit= "Spades"),
            Card(rank= "Ace", suit= "Clubs")
        ]

        validator = PairValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_return_pairs_from_card_collection(self):
        ten_of_spades = Card(rank = "10", suit = "Spades")
        ten_of_clubs = Card(rank = "10", suit = "Clubs")

        cards = [
            Card(rank = "3", suit = "Hearts"),
            Card(rank = "5", suit = "Diamonds"),
             ten_of_clubs,
            ten_of_spades,
            Card(rank = "King", suit = "Clubs")
        ]

        validator = PairValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [ten_of_clubs, ten_of_spades]
        )




 