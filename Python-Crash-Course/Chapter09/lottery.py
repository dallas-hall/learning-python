#!/usr/bin/env python3
import logging, sys, os, time
from random import randint, choice, shuffle

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.100)


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


def get_n_random_chars_from_list(n, a_list):
	# Copy the list
	random_list = a_list
	# Convert to set to remove duplicates and convert back to list
	random_list = list(set(random_list))
	# Shuffle the list and return the first 5 chars.
	shuffle(random_list)
	return random_list[:n]


lottery_seed_numbers = []
lottery_seed_numbers += get_n_random_numbers_as_list(10, 0, 9)
lottery_seed_numbers += get_n_random_capital_letters_as_list(5)
print(lottery_seed_numbers)
lottery_numbers = get_n_random_chars_from_list(5, lottery_seed_numbers)
print(lottery_numbers)

my_ticket = []
counter = 0
while True:
	my_ticket += get_n_random_numbers_as_list(10, 0, 9)
	my_ticket += get_n_random_capital_letters_as_list(5)
	my_ticket = get_n_random_chars_from_list(5, my_ticket)

	print(my_ticket)
	# Convert to set so it's easier to compare.
	if set(lottery_numbers) != set(my_ticket):
		counter += 1
	else:
		break
print(f"The lottery numbers were {lottery_numbers}.")
print(f"Your ticket numbers were {my_ticket}.")
print(f"You won the lottery after {counter} attempts at getting the winning ticket.")
