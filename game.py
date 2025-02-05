import random

# generate random number
number = random.randint(1, 10)

# prompt user to enter name
player_name = input("Hello, What's your name?")

# add variable to store number of guesses, iterate(+1) this value each time user guesses
number_of_guesses = 0

# print string with user_name in it
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

# create a while loop to iterate through the number_of_guesses value while it is lower than 5, when > 5 player loses
# define the controlling expression of the while loop
while number_of_guesses < 5:
    # take the input from the user and store it in the guess variable   
    # user input is a string object; we need to convert it to an integer using Python's int() method. 
    guess = int(input())
    # incremember number_of_guesses value
    number_of_guesses +=1

    # add an if clause to return computer prompt based on value of number vs value of guess, while number_of_guesses < 5
        # condition 1: number is greater than guess; 'guess is too low'
        # condition 2: number is less than guess; 'guess is too high'
        # condition 3: break; terminate the loop when the guess is equal to the generated number.

    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        break

    if guess == number:
        print('Congratulations, ' + player_name + '! You guessed the number in ' + str(number_of_guesses) + ' tries!')
    else:
        print('Sorry, ' + player_name + ', you did not guess the number. The number was ' + str(number))