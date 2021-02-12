class Player():
    def __init__(self, name, hand):
        self.hand = hand
        self.name = name 

    def __gt__(self, other):
        current_player_best_validator_index = self.best_hand()[0]
        other_player_best_validator_index = other.best_hand()[0]
        return current_player_best_validator_index < other_player_best_validator_index
        
    def best_hand(self):
        return self.hand.best_rank()

    def add_cards(self, cards):
        self.hand.add_cards(cards)

    def want_to_fold(self):
        return False
        #Wage development on hold. Ismail continue 
