#!/usr/bin/env python3
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

peperoni_pizza = {
	'crust': 'thin',
	'price': 5.99,
	# Using a nested list so we can have more than one value inside the key value pair
	'ingredients': ['tomato sauce', 'cheese', 'pepperoni'],
	'custom toppings': []
}
print("# Printing standard pepperoni pizza.")
# Omitting .keys() as to demonstrate that looping through keys is the default behaviour.
for key in peperoni_pizza:
	if key == 'price':
		print(key.title() + ": $" + str(peperoni_pizza.get(key)))
	elif key == 'ingredients' or key == 'custom toppings':
		print(key.title() + ": ")
		for i in range(len(peperoni_pizza.get(key))):
			print("\t* " + peperoni_pizza.get(key)[i].title())
	else:
		print(key.title() + ": " + peperoni_pizza.get(key).title())

print("Adding some custom toppings.")
peperoni_pizza.get('custom toppings').append('extra cheese')
peperoni_pizza.get('custom toppings').append('extra peperoni')

print("\n# Printing customised pepperoni pizza.")
for key in peperoni_pizza.keys():
	if key == 'price':
		print(key.title() + ": $" + str(peperoni_pizza.get(key)))
	elif key != 'ingredients' and  key != 'custom toppings':
		print(key.title() + ": " + str(peperoni_pizza.get(key)).title())
	else:
		print(key.title() + ": ")
		for i in range(len(peperoni_pizza.get(key))):
			print("\t* " + peperoni_pizza.get(key)[i].title())
