#!/usr/bin/python3
import logging
import os
import sys
import time
# Needed to right click Chapter08 > Mark directory as > Sources Root
import pizza

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

pizza.make_pizza_args("family", "barbeque sauce", "cheese", "pepperoni", "ham", "beef")
pizza.make_pizza_kwargs("medium", toppings=["tomato paste", "cheese", "pepperoni"])