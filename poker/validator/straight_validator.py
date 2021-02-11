from poker.validator import FiveCardRanksInARowValidator

class StraightValidator(FiveCardRanksInARowValidator):
    def __init__(self, cards):
        self.cards = cards 

    def is_valid(self):
        return len(self._collection_of_five_straight_cards_in_a_row) >= 1
        
    def valid_cards(self):
        return self._collection_of_five_straight_cards_in_a_row[-1]



     