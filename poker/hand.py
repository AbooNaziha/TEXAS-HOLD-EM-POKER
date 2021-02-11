from poker.validator import (
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    PairValidator,
    HighCardValidator,
    NoCardValidator
)

class Hand():
    def __init__(self):
        self.cards = []

    def __repr__(self):
        cards_as_strings = [str(card) for card in self.cards]
        return ", ".join(cards_as_strings)

    def add_cards(self, cards):
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy

    @property
    def _rank_validator_from_best_to_worst(self):
        return (
            ("Royal Flush", self._royal_flush),
            ("Straight Flush", self._straight_flush),
            ("Four of a Kind", self._four_of_a_kind),
            ("Full House", self._full_house),
            ("Flush", self._flush),
            ("Straight", StraightValidator(cards = self.cards).is_valid),
            ("Three of a Kind", ThreeOfAKindValidator(cards = self.cards).is_valid),
            ("Two Pair", TwoPairValidator(cards = self.cards).is_valid),
            ("Pair", PairValidator(cards = self.cards).is_valid),
            ("High Card", HighCardValidator(cards = self.cards).is_valid),
            ("No Card", NoCardValidator(cards = self.cards).is_valid)
        )
 
    def best_rank(self):
        for rank in self._rank_validator_from_best_to_worst:
            name, validator_func = rank
            if validator_func():
                return name

    def _royal_flush(self):
        is_straight_flush = StraightValidator(cards = self.cards).is_valid()
        if not is_straight_flush:
            return False
        is_royal = self.cards[-1].rank == "Ace"
        return is_straight_flush and is_royal
    
    def _straight_flush(self):
        return self._flush() and StraightValidator(cards = self.cards).is_valid()

    def _four_of_a_kind(self):
        ranks_with_four_of_a_kind = self._ranks_with_count(4)
        return len(ranks_with_four_of_a_kind) == 1

    def _full_house(self):
        return ThreeOfAKindValidator(cards = self.cards).is_valid() and PairValidator(cards = self.cards).is_valid()

    def _flush(self):
        suits_that_occur_5_or_more_time = {
            suit: suit_count
            for suit, suit_count in self._card_suit_count.items()
            if suit_count >= 5
        }

        return len(suits_that_occur_5_or_more_time) == 1
       
    def _ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_count.items()
            if rank_count == count
        }

    
    @property
    def _card_suit_count(self):
        card_suit_count = {}
        for card in self.cards:
            card_suit_count.setdefault(card.suit, 0)
            card_suit_count[card.suit] += 1
        return card_suit_count


    @property
    def _card_rank_count(self):
        card_rank_count = {}
        for card in self.cards:
            card_rank_count.setdefault(card.rank, 0)
            card_rank_count[card.rank] += 1
        return card_rank_count
