import random, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
logging.debug('Starting program.')
guess = ''
logging.debug('Initialised guess as \'' + str(guess) + '\'')
while guess not in ('heads', 'tails'):
	print('Guess the coin toss. Enter heads or tails: ')
	guess = input()
	logging.debug('Read in guess as \'' + str(guess) + '\'')

toss = random.randint(0, 1) # 0 is tails and 1 is heads
logging.debug('Initialised toss as \'' + str(toss) + '\'')
logging.debug('Checking if guess \'' + str(guess) + '\' equals toss ' + '\'' + str(toss) + '\'')
# bug here, the guess is never mapped to the number 0 or 1
if toss == guess:
	print('You got it.')
else:
	print('Guess again...')
	# bug here, should be guess
	guesss = input()
	logging.debug('Checking if guess \'' + str(guess) + '\' equals toss ' + '\'' + str(toss) + '\'')
	if toss == guess:
		print('You got it.')
	else:
		print('You suck!')
logging.debug('Finishing program.')