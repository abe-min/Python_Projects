import random

#Here are a list of words from which the game will randomly select a word for the user to guess
list_of_words = ['python', 'java', 'swift', 'javascript']
chosen_word = random.choice(list_of_words)
chosen_hidden_word = ("-"*(len(chosen_word)-3))
#Ask the user to enter a word
user_guess = input("Please guess the word " + chosen_word[:3] + chosen_hidden_word + " ") #Include the first 3 characters of the word as a hint


#Check if the user selection is correct
if user_guess == chosen_word:
    print("You survived!")
else:
    print("You lost!")