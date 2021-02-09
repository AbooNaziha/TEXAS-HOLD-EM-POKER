import unittest

from poker.card import Card

from poker.validator import NoCardValidator

class NoCardValidatorTest(unittest.TestCase):
    def test_validates_that_no_card_are_present(self):
       validator = NoCardValidator(cards = [])
       
       self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_no_valid_cards(self):
        validator = NoCardValidator(cards = [])

        self.assertEqual(
            validator.valid_cards(),
            []
        )