import random

# Create a list of words.
word_list = ["banana", "strawberry", "raspberry", "orange", "kiwi"]
print(word_list)

# Choose a word at random.
word = random.choice(word_list)

print(word)

# Get an input from user and save into a variable.

guess = input("What's your first letter: ")

# Check if the user's input is valid.

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")