import random

# generate random number
number = random.randint(1, 10)

# prompt user to enter name
player_name = input("Hello, What's your name?")

# add variable to store number of guesses, iterate(+1) this value each time user guesses
number_of_guesses = 0

# print string with user_name in it
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')