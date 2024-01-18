#!/usr/bin/env python3
import logging
import os
import sys
import time

# Import everything from pizza.py.
# Same as `from pizza import *` but don't use this as you can have function and variable naming collisions.
# Needed to right click Chapter08 > Mark directory as > Sources Root
import pizza
# Import 1 function from pizza.py
from pizza import make_pizza_kwargs
# Import 1 function from pizza.py and rename it.
from pizza import rename_me_after_importing as print_msg
# Import 1 function from pizza.py and rename the module.
import pizza as p

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.100)

# Call using `import pizza`
pizza.make_pizza_args("family", "barbeque sauce", "cheese", "pepperoni", "ham", "beef")
# Call using `from pizza import make_pizza_kwargs`
make_pizza_kwargs("medium", toppings=["tomato paste", "cheese", "pepperoni"])
# Call using `from pizza import rename_me_after_importing as print_msg`
print_msg("Hello, world!")
# Call using `import pizza as p`
p.rename_me_after_importing("Hello, world!")
