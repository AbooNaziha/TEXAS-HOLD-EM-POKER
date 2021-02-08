class Player():
    def __init__(self, name, hand):
        self.hand = hand
        self.name = name 

    def best_hand(self):
        return self.hand.best_rank()

    def add_cards(self, cards):
        self.hand.add_cards(cards)

    def want_to_fold(self):
        return False
        #Wage development on hold. Ismail continue 