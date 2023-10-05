import random

# Create a list of your favorite fruits
word_list = ["apple", "banana", "strawberry", "kiwi", "orange"]

class Hangman:
    def __init__(self, word_list, num_lives=5):
        
        self.word = random.choice(word_list)
        self.num_lives = num_lives
        self.word_list = word_list
        self.word_guess = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    # Function to check if guess is in word.
    def check_guess(self, guess):

        letter = guess.lower()

        # Check if the guessed letter is in the secret word.    
        if letter in self.word:
            print(f'Good guess! {letter} is in the word.')

        else:
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives left.')
            print(f'Sorry, {letter} is not in the word. Try again') 

    # Function to ask for the input and use check_guess.
    def ask_for_input(self):

        while True:
            
            # Get the first letter from the player.

            guess = input("\n What's your guess: ")

            # Check if the user's input is a single letter and is a letter.

            if len(guess) != 1 and guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            else:
                self.check_guess(guess)  
                self.list_of_guesses.append(guess)
                for position, letter in enumerate(self.word):
                    if letter == guess:
                        self.word_guess[position] = letter
                    else:
                        pass
                self.num_letters -= 1
                [print(item, end='') for item in self.word_guess]
hang_game = Hangman(word_list)
hang_game.ask_for_input()
