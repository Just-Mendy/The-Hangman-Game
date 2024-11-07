import random
import os
import logging


class MultiplayerHangman:
    WORD_FILES = {
        "colours": "colours_words.txt",
        "animals": "animal_words.txt",
        "countries": "country_words.txt"
    }

    def __init__(self, category, num_players=2):
        self.category = category.lower()
        self.word_list = self._load_words()
        self.word = random.choice(self.word_list).upper()
        self.num_players = num_players
        self.players = [f"Player {i+1}" for i in range(num_players)]
        self.current_player = 0
        self.guesses_left = 6
        self.guessed_letters = set()
        self.word_completion = "_" * len(self.word)
        self.hints_left = 3
        self.hangman_stages = [
            """
               +---+
               |   |
                   |
                   |
                   |
                   |
            =========
            """,
            """
               +---+
               |   |
               O   |
                   |
                   |
                   |
            =========
            """,
            """
               +---+
               |   |
               O   |
               |   |
                   |
                   |
            =========
            """,
            """
               +---+
               |   |
               O   |
              /|   |
                   |
                   |
            =========
            """,
            """
               +---+
               |   |
               O   |
              /|\\  |
                   |
                   |
            =========
            """,
            """
               +---+
               |   |
               O   |
              /|\\  |
              /    |
                   |
            =========
            """,
            """
               +---+
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
            =========
            """
        ]

    def _load_words(self):
        filename = self.WORD_FILES.get(self.category)
        if filename:
            file_path = os.path.join(os.path.dirname(__file__), filename)
            with open(file_path, 'r') as file:
                return [line.strip().upper() for line in file.readlines()]
        else:
            print("Invalid category.")
            return []

    def guess(self, letter):
        letter = letter.upper()
        if letter in self.guessed_letters:
            print("You already guessed that letter.")
            return
        elif letter == self.word:
            self.word_completion = self.word
        elif len(letter) == 1:
            self._single_letter_guess(letter)
        else:
            print("Incorrect guess.")
            self.guesses_left -= 1
        self.guessed_letters.add(letter)

    def _single_letter_guess(self, letter):
        if letter not in self.word:
            print("Incorrect guess.")
            self.guesses_left -= 1
        else:
            print("Correct guess!")
            self._update_completion(letter)

    def _update_completion(self, letter):
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.word_completion = self.word_completion[:i] + letter + self.word_completion[i+1:]

    def give_hint(self):
        if self.hints_left > 0:
            hint_letter = random.choice([letter for letter in self.word if letter not in self.guessed_letters])
            print(f"Hint: Try the letter '{hint_letter}'")
            self.hints_left -= 1
        else:
            logging.info("No hints left.")
            print("No hints left.")

    def display_progress(self):
        print("Word:", " ".join(self.word_completion))
        print("Guesses left:", self.guesses_left)
        print(self.hangman_stages[6 - self.guesses_left])   

    def is_game_over(self):
        if self.guesses_left <= 0:
            print("You lose! The word was", self.word)
            return True
        elif "_" not in self.word_completion:
            print("Congratulations! You guessed the word:", self.word)
            return True
        return False


def main():
    print("Welcome to Multiplayer Hangman!")
    print("Available categories:", ", ".join(MultiplayerHangman.WORD_FILES.keys()))
    category = input("Choose a category: ").lower()
    num_players = int(input("Enter the number of players: "))
    game = MultiplayerHangman(category, num_players)
    while not game.is_game_over():
        game.display_progress()
        print(f"{game.players[game.current_player]}'s turn:")
        guess = input("Guess a letter or type the entire word or '#' for a hint: ").upper()
        if guess == '#':
            game.give_hint()
        else:
            game.guess(guess)
        game.current_player = (game.current_player + 1) % game.num_players
        if "_" not in game.word_completion:
            break
    print("Game over.")


if __name__ == "__main__":
    main()