# Hangman

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Description

The Hangman project is a classic word-guessing game implemented in Python. The aim of the project is to create an interactive game where the computer selects a secret word, and the user tries to guess it letter-by-letter. The user has a limited number of attempts, and for each incorrect guess, a part of the hangman is drawn. The user wins if they guess the word before the hangman is fully drawn, and they lose if the hangman is completed before they guess the word.

### What I Learned
- How to use Git for version control.
- Implementing classes to organize code and improve code readability.
- Utilizing encapsulation and abstraction principles to manage game state and user interaction.

## Installation

To run the Hangman game, follow these steps:

1. Clone the repository to your local machine using Git:
   ```bash
   git clone https://github.com/your-username/hangman.git
2. Navigate to the project directory:
   ```bash
   cd hangman
3. Run the game script:
   ```bash
   python3 hangman.py

## Usage

1. Start the game by running the script as mentioned in the Installation instructions.
2. The computer will select a random word, and you'll be prompted to guess one letter at a time.
3. Guess letters one by one until you either guess the entire word or run out of attempts.
4. If you guess the word correctly before you run out of attempts you win!

## File Structure

The project file structure is organized as follows:
```bash
hangman/
│
├── hangman.py           # Main game script
├── words.txt            # Text file containing a list of words for the game
└── README.md            # Project documentation (this file)