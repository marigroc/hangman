# Hangman

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Description

The Hangman project is a classic word-guessing game implemented in Python. The aim of the project is to create an interactive game where the computer selects a secret word, and the user tries to guess it letter-by-letter. The user has a limited number of attempts. The user wins if they guess the word before they run out of the attempts, and they lose if the hangman is "completed" before they guess the word.

### What I Learned
- Implementing classes to organize code and improve code readability.
- Utilizing encapsulation and abstraction principles to manage game state and user interaction.
- Handling correct user input for single alphabetical characters.
- Tracking and displaying game progress, including guessed letters and remaining lives.
- Troubleshooting for the infinite loops and how to fix them.


## Installation

To run the Hangman game, follow these steps:

1. Clone the repository to your local machine using Git:
   ```bash
   git clone https://github.com/marigroc/hangman.git
2. Navigate to the project directory:
   ```bash
   cd hangman
3. Run the game script:
   ```bash
   python3 hangman.py

## Usage

1. Start the game by running the script as mentioned in the Installation instructions.
2. The computer will select a random word from the provided word list, and you'll be prompted to guess one letter at a time.
3. Guess letters one by one until you either guess the entire word or run out of lives.
4. The game will display whether your guesses are correct or not and update the word with correctly guessed letters.
5. The number of remaining lives will be shown after each incorrect guess.
6. If you guess the entire word before running out of lives, you win!

## File Structure

The project file structure is organized as follows:
```bash
hangman/
│
├── hangman.py           # Main game script.
├── milestone_2.py       # Basic functionality of the game with simple code.
├── milestone_3.py       # Rebuilt functions with added complexity.
├── milestone_4.py       # Third step in building complex code.
├── words.txt            # Text file containing a list of words for the game.
└── README.md            # Project documentation (this file).
```


## License

This project is licensed under the MIT License

