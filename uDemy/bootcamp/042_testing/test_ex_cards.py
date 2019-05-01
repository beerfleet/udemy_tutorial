import unittest
from robot import Robot
from ex_cards import Card, Deck

class CardTests(unittest.TestCase):
    def setUp(self):
        self.suits = Deck.suits
        self.values = Deck.values
        self.card = Card(self.suits[0], self.values[0])
        self.deck = Deck()

    def test_card_create(self):
        self.assertEqual(
            self.card.suit, 
            "Hearts",
            f"The card should be {self.suits[0]}"
        )

if __name__ == "__main__":
    unittest.main()