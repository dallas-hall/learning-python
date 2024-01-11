#!/usr/bin/env python
import logging, sys, os, time

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.100)


# The * makes an empty tuple and every argument that is supplied is put into that tuple.
# Typically, this is called *args
def make_small_pizza(*toppings):
	print("The small pizza will have the following toppings:")
	for topping in toppings:
		print(f"\t* {topping}")


# Mixing positional and arbitrary arguments. Positional always go first.
def make_pizza(size, *toppings):
	print(f"The {size} pizza will have the following toppings:")
	for topping in toppings:
		print(f"\t* {topping}")


make_small_pizza("tomato paste", "cheese", "pepperoni")
make_small_pizza("barbeque sauce", "cheese", "pepperoni", "ham", "beef")

# The first argument is treated as a positional arugment and the rest are packed into the arg tuple
make_pizza("size", "tomato paste", "cheese", "pepperoni")
make_pizza("medium", "tomato paste", "cheese", "pepperoni", "jalepenos")
make_pizza("family", "barbeque sauce", "cheese", "pepperoni", "ham", "beef")
