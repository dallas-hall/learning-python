# import the random module
import random


# define a function that takes an argument
def get8BallAnswer(inputNumber):
	if inputNumber == 1:
		return 'It is certain'
	elif inputNumber == 2:
		return 'It is decidedly so'
	elif inputNumber == 3:
		return 'Yes'
	elif inputNumber == 4:
		return 'Reply hazy try again'
	elif inputNumber == 5:
		return 'Ask again later'
	elif inputNumber == 6:
		return 'Concentrate and ask again'
	elif inputNumber == 7:
		return 'My reply is no'
	elif inputNumber == 8:
		return 'Outlook not so good'
	elif inputNumber == 9:
		return 'Very doubtful'


# generate a pseudo-random number using the random number module, which is between 1 and 9 (inclusive)
prn = random.randint(1, 9)

# call the function and store the returned value
yourFortune = get8BallAnswer(prn)

# print the value
print(yourFortune)
