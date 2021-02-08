import unittest
from unittest.mock import MagicMock

from poker.hand import Hand
from poker.player import Player 

class PlayerTest(unittest.TestCase):
    def test_stores_name_and_hand(self):
        hand = Hand(cards = [])
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
