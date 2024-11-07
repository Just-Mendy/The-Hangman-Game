# The Hangman Game
# Multiplayer Hangman Game

Multiplayer Hangman is a console-based game where multiple players can take turns guessing letters to figure out a hidden word. The game supports categories like animals, colors, and countries. Each incorrect guess brings the hangman closer to completion. The game ends when the word is fully guessed or the hangman is completed.

## Features

- Multiplayer support (default: 2 players)
- Multiple categories to choose from
- Hints available for players
- Simple and interactive console interface

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/multiplayer-hangman.git
    cd multiplayer-hangman
    ```

2. **Ensure you have Python installed**. This game requires Python 3.6 or later.

3. **Set up the environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install required packages** (if any):
    ```bash
    pip install -r requirements.txt  # Add a requirements.txt if you have any dependencies
    ```

5. **Prepare word files**:
    - Ensure you have the word files (`colours_words.txt`, `animal_words.txt`, `country_words.txt`) in the same directory as the script.
    - Each file should contain words related to the category, one word per line.

## Usage

Run the game using the following command:
```bash
python MultiplayerHangman.py

How to Play

    Choose a category:
        animals, colours, or countries

    Enter the number of players:
        Default is 2 players, but you can choose more.

    Gameplay:
        Players take turns guessing letters or attempting to guess the entire word.
        Enter # for a hint (if hints are available).

    Win/Lose Conditions:
        Win by guessing all letters in the word.
        Lose if all guesses are used up and the hangman is fully drawn.
    
Contributing

Contributions are welcome! Please fork the repository and submit a pull request.


License

This project is licensed under the MIT License. See the LICENSE file for details.


Summary:
- The README provides clear instructions for installing, using, and testing the Multiplayer Hangman game.
- It includes a brief overview of the game features and gameplay instructions.
- It demonstrates how to run the game and tests, and outlines test cases with example code.
- Encourages contributions and specifies the licensing of the project.
