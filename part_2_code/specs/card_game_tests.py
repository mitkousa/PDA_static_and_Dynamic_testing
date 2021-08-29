import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Ace", 1)
        self.card2 = Card("Diamond", 5)
        self.card3 = Card("Spade", 4)
        self.cardgame = CardGame()
        self.cards = [self.card1, self.card2, self.card3]
  
    def test_check_for_ace_value_is_1(self):
        self.assertEqual(True, self.cardgame.check_for_ace(self.card1))

    def test_highest_card(self):
        self.assertEqual(5, self.cardgame.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 10", self.cardgame.cards_total(self.cards))