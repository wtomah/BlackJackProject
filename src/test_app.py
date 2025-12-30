import unittest
from main import BlackJack

class TestBlackJack(unittest.TestCase):

    def test_hand(self):
        hand = [11, 11, 10]
        self.assertEqual(BlackJack.calculate_score(hand), 12)

if __name__ == '__main__':
    unittest.main()