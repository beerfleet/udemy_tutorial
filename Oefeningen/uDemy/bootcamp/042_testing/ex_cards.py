from random import shuffle

class Card:    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

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
        return "Deck of {} cards".format(self.count())

    def __iter__(self):
        card_iterator = iter(Deck.cards)
        while True:
            try:
                card = next(card_iterator)
            except StopIteration:
                break            


    def _deal(self, amount):
        to_deal = []
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        if self.count() >= amount:
            for n in range(0, amount):
                to_deal.append(Deck.cards.pop())            
        elif self.count() < amount:
            for n in range(0, self.count()):
                to_deal.append(Deck.cards.pop())        
        return to_deal


    def count(self):
        return len(Deck.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, size):
        return self._deal(size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(Deck.cards)
        return self

deck = Deck()
print(deck)
deck.shuffle()

hand = deck.deal_hand(45)
hand = deck.deal_hand(5)
hand = deck.deal_hand(5)


print(hand)