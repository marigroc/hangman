import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game.
        
        Args:
            word_list (list): A list of words to choose from.
            num_lives (int): The number of lives the player has (default is 5).
        """
        self.word = random.choice(word_list)
        self.num_lives = num_lives
        self.word_list = word_list
        self.word_guess = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    # Private method to check if guess is in word.
    def _check_guess(self, guess):
        """
        Check if the guessed letter is in the secret word.
        
        Args:
            guess (str): The guessed letter.
        """
        guess = guess.lower()

        # Check if the guessed letter is in the secret word.    
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')

        else:
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives left.')
            print(f'Sorry, {guess} is not in the word. Try again') 

    # Public method to ask for the input and use _check_guess.
    def ask_for_input(self):
        """
        Ask the player for a letter guess and process it.
        """
        while True:
            
            # Get the first letter from the player.

            guess = input("\n What's your guess: ")

            # Check if the user's input is a single letter and is a letter.

            if len(guess) != 1 and guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            else:
                self._check_guess(guess)  
                self.list_of_guesses.append(guess)

                # Update the word_guess with correctly guessed letters
                for position, letter in enumerate(self.word):
                    if letter == guess:
                        self.word_guess[position] = letter
                    else:
                        pass
                self.num_letters -= 1
                # Print the current word_guess
                [print(item, end='') for item in self.word_guess]


# Create a list of your favorite fruits
word_list = ["apple", "banana", "strawberry", "kiwi", "orange"]
# Create an instance of the Hangman class and start the game
hang_game = Hangman(word_list)
hang_game.ask_for_input()
