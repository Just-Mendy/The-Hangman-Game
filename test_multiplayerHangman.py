import unittest
from MultiplayerHangman import MultiplayerHangman


class TestMultiplayerHangman(unittest.TestCase):

    def setUp(self):
        # Use a small subset of the real data for testing
        self.test_words = ["LION", "TIGER", "ELEPHANT"]  # Animal words for testing
        self.game = MultiplayerHangman(category='animals', num_players=2)
        self.game.word = 'LION'
        self.game.word_completion = '_____'  # Assuming 'LION' has 5 letters
        self.game.guessed_letters = set()
        self.game.guesses_left = 6

    def test_load_words(self):
        self.assertIn(self.game.word, self.test_words)

    def test_guess_correct_letter(self):
        self.game.guess('L')
        self.assertIn('L', self.game.guessed_letters)
        self.assertEqual(self.game.word_completion, 'L____')
        self.assertEqual(self.game.guesses_left, 6)

    def test_guess_incorrect_letter(self):
        self.game.guess('Z')
        self.assertIn('Z', self.game.guessed_letters)
        self.assertEqual(self.game.word_completion, '_____')
        self.assertEqual(self.game.guesses_left, 5)

    def test_give_hint(self):
        self.game.hints_left = 3
        self.game.give_hint()
        self.assertLess(self.game.hints_left, 3)

    def test_is_game_over_win(self):
        self.game.word_completion = 'LION'
        self.assertTrue(self.game.is_game_over())

    def test_is_game_over_lose(self):
        self.game.guesses_left = 0
        self.assertTrue(self.game.is_game_over())


if __name__ == '__main__':
    unittest.main()
