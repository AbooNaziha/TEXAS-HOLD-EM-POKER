class FlushValidator():
    def __init__(self, cards):
        self.cards = cards 

    
    def is_valid(self):
        return len(self._suit_that_occur_five_or_more_times) == 1

    def valid_cards(self):
        cards = [card for card in self.cards if card.suit in self._suit_that_occur_five_or_more_times]

        return cards[-5:]

    @property
    def _card_suit_count(self):
        card_suit_count = {}
        for card in self.cards:
            card_suit_count.setdefault(card.suit, 0)
            card_suit_count[card.suit] += 1
        return card_suit_count

    @property
    def _suit_that_occur_five_or_more_times(self):
        return {
            suit: suit_count
            for suit, suit_count in self._card_suit_count.items()
            if suit_count >= 5
        }
