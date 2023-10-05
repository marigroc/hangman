import random

# Create a list of your favorite fruits
word_list = ["apple", "banana", "strawberry", "kiwi", "orange"]

# Choose a random word from the word_list
word = random.choice(word_list)

# Function to check if guess is in word.
def check_guess(guess):

    guess_lower = guess.lower()

    # Check if the guessed letter is in the secret word.    
    if guess_lower in word:
        print(f'Good guess! {guess_lower} is in the word.')

    else:
        print(f'Sorry, {guess_lower} is not in the word. Try again') 

# Function to ask for the input and use check_guess.
 
def ask_for_input():

    

    while True:
        
        # Get the first letter from the player.

        guess = input("What's your first guess: ")

        # Check if the user's input is a single letter and is a letter.

        if len(guess) == 1 and guess.isalpha():
            print("Good guess!")
            break

        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess)

ask_for_input()