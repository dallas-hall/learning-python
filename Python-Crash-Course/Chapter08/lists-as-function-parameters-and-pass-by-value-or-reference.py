#!/usr/bin/python3
import logging, sys, os, time
from pprint import pprint

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)


def pretty_print_list(list, list_name):
	print(f"{list_name} is:")
	pprint(list)


# Everything from print_queue will be inside printed_items after this function
def print_queue_items(print_queue, printed_items):
	for i in range(len(print_queue)):
		# Use .pop to get the last item of the list
		current_print_item = print_queue.pop()
		print(f"Printing {current_print_item}")
		printed_items.append(current_print_item)


def show_printed_items(printed_items):
	print("The following items have been printed:")
	for i in range(len(printed_items)):
		print(f"\t* {printed_items[i]}")


print_queue = ['resume', 'letter', 'picture']
printed_items = []


# print_queue will not be empty after this function because we are using pass by value
# Pass by value is done by using slice [:] to copy the list
print_queue_items(print_queue[:], printed_items)
show_printed_items(printed_items)
pretty_print_list(print_queue, "print_queue")
printed_items.clear()

# We are directly manipulating the lists within the function.
# print_queue will be empty after this function because we are using pass by reference
print_queue_items(print_queue, printed_items)
show_printed_items(printed_items)
pretty_print_list(print_queue, "print_queue")

