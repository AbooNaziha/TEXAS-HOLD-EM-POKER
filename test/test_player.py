import unittest
from unittest.mock import MagicMock

from poker.card import Card
from poker.hand import Hand
from poker.player import Player 

class PlayerTest(unittest.TestCase):
    def test_stores_name_and_hand(self):
        hand = Hand()
        player = Player(name = "Ismail", hand = hand)
        self.assertEqual(player.name, "Ismail")
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Straight Flush"
        player = Player(name = "Ismail", hand = mock_hand)

        self.assertEqual(
            player.best_hand(),
            "Straight Flush"
        )

        mock_hand.best_rank.assert_called()

    def test_passes_new_card_to_hand(self):
        mock_hand = MagicMock()
        player = Player(name = "Munira", hand = mock_hand)

        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Queen", suit = "Diamonds")
        ]


        player.add_cards(cards)

        mock_hand.add_cards.assert_called_once_with(cards)

    
    def test_decides_to_continue_or_drop_out_of_games(self):
        player = Player(name = "Nafisa", hand = Hand())
        self.assertEqual(
            player.want_to_fold(),
            False
        )
    
    def test_player_is_sorted_by_best_hand(self):
        mock_hand1 = MagicMock()
        mock_hand1.best_rank.return_value = (0, "Royal Flush", [])

        mock_hand2 = MagicMock()
        mock_hand2.best_rank.return_value = (2, "Four of a Kind", [])

        player1 = Player(name = "Susan", hand = mock_hand1)
        player2 = Player(name = "Aisha", hand = mock_hand2)

        players = [player1, player2]

        self.assertEqual(
            max(players),
            player1
        )