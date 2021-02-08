class Player():
    def __init__(self, name, hand):
        self.hand = hand
        self.name = name 

    def best_hand(self):
        return self.hand.best_rank()