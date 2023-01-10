import random

#Ask the user to enter a word
user_guess = input("Please guess a word: ")

#Here are a list of words from which the game will randomly select a word for the user to guess
list_of_words = ['python', 'java', 'swift', 'javascript']
chosen_word = random.choice(list_of_words)

#Check if the user selection is correct
if user_guess == chosen_word:
    print("You survived!")
else:
    print("You lost!")