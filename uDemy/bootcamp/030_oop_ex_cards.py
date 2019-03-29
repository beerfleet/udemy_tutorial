from random import shuffle

class Card:    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:    
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    cards = []

    def __init__(self):
        Deck.cards = []
        for suit in Deck.suits:
            for value in Deck.values:
                Deck.cards.append(Card(suit, value))

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def _deal(self, amount):
        to_deal = []        
        if self.count() >= amount:
            for n in range(0, amount):
                to_deal.append(Deck.cards.pop())
            return to_deal
        else:
            raise ValueError("All cards have been dealt")

    def count(self):
        return len(Deck.cards)

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, size):
        return self._deal(size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(Deck.cards)

deck = Deck()
deck.shuffle()
print(deck)
hand = deck.deal_hand(5)
deck = Deck()
deck.shuffle()
print(hand)