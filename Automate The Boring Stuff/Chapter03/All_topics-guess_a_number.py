# import the PRN module 
import random
# get a PRN between 1 and 20, both are inclusive
answer = random.randint(1, 20)
print('Pick a number between 1 and 20, you have 6 attempts to guess it.')

# a for loop that starts at min (1) and stops at max - 1 (7 - 1 = 6)
for amountOfGuesses in range(1, 7):
    print('Enter your guess.')
    # validate the users input in try / except block
    try:
        # create a global variable
        global guess
        # try to cast from string to int, input() returns a string
        guess = int(input())
    # catch input errors for user input that isn't an int
    except ValueError:
        print('Your input wasn''t an integer, try again.\nYou have used 1 attempt though.')
        # skip this loop step and go to the next one
        continue
    
    # check the user input against the answer
    if guess < answer:
        print('Too low...')
    elif guess > answer:
        print('Too high...')
    else:
        # exit if the answer was correct
        break
    
# display final output to the user, the first is if the user guessed the number
# remember the numbers need to be casted to strings with str() when printed
if guess == answer:
    print('Correct! It took you ' + str(amountOfGuesses) + ' attempts to guess ' + str(answer) + '.')
# the user didn't guess the number and the for loop finished
else:
    print('You ran out of guesses, the number was ' + str(answer) + '.')     
    