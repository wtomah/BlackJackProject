import unittest
from main import BlackJack

class TestBlackJack(unittest.TestCase):

    def test_hand(self):
        hand = [2, 4, 10]
        self.assertEqual(BlackJack.calculate_score(hand), 16, "Valid Hand")
    
    def test_opponent(self):
        user_score = 14
        opponent_score = 19
        self.assertEqual(BlackJack.compare(user_score, opponent_score), "You lose.")

    def test_user(self):
        user_score = 18
        opponent_score = 17
        self.assertEqual(BlackJack.compare(user_score, opponent_score), "You win!")

    def test_draw(self):
        user_score = 19
        opponent_score = 19
        self.assertEqual(BlackJack.compare(user_score, opponent_score), "It's a draw!")

    def test_start(self):
        input = '9'
        self.assertEqual(BlackJack.get_start_choice(input), "Invalid input. Please enter 'y' or 'n'.")
    

if __name__ == '__main__':
    unittest.main()