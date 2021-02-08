import unittest
from unittest.mock import patch

from poker.card import Card
from poker.deck import Deck

class DectTest(unittest.TestCase):
    def test_has_length_that_is_equal_to_counts_of_cards(self):
        deck = Deck()

        self.assertEqual(
            len(deck),
            0
        )

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

    @patch('random.shuffle')
    def test_shuffle_card_in_random_order(self, mock_shuffle):
        deck = Deck()
        
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "8", suit = "Diamonds")
        ]
        
        deck.add_cards(cards)

        deck.shuffle()

        mock_shuffle.assert_called_once_with(cards)

    def test_remove_specified_number_of_card_from_deck(self):
        ace = Card(rank = "Ace", suit = "Spades")
        eight = Card(rank = "8", suit = "Diamonds")
        cards = [ace, eight]

        deck = Deck()
        deck.add_cards(cards)

        self.assertEqual(
            deck.remove_card(1),
            [ace]
        )

        self.assertEqual(
            deck.cards,
            [eight]
        )