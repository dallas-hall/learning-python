import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Starting program.')

def factorial(n):
	logging.debug('Start of factorial(%s)' % (n))
	total = 1
	# The bug is i starting at 0
	for i in range(n + 1):
	# This fix is
	# for i in range(1, n + 1):
		total *= i
		logging.debug('i is ' + str(i) + ', total is ' + str(total))
	logging.debug('End of factorial(%s)' % (n))
	return total


answer = factorial(5)
print(answer)
logging.debug('End of program.')

