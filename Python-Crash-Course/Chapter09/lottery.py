#!/usr/bin/python3
import logging, sys, os, time
from random import randint

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)


def get_n_random_numbers_as_list(n, start, end):
	numbers = []
	for i in range(0, n):
		numbers.append(randint(start, end))
	return numbers


def get_n_random_capital_letters_as_list(n):
	letters = []
	for i in range(0, n):
		letters.append(chr(randint(65, 90)))
	return letters


lottery_numbers = []
lottery_numbers += get_n_random_numbers_as_list(10, 1, 100)
lottery_numbers += get_n_random_capital_letters_as_list(5)
print(lottery_numbers)

my_ticket = []
my_ticket += get_n_random_numbers_as_list(10, 1, 100)
my_ticket += get_n_random_capital_letters_as_list(5)

counter = 0
if set(lottery_numbers) == set(my_ticket):
	counter += 1
else:
	while set(lottery_numbers) != set(my_ticket):
		counter += 1
		my_ticket = []
		my_ticket += get_n_random_numbers_as_list(10, 1, 100)
		my_ticket += get_n_random_capital_letters_as_list(5)
print(f"You won the lottery after {counter} attempts at getting the winning ticket.")


