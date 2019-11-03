#!/usr/bin/python3
import logging, sys, os, time

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

peperoni_pizza = {
	'crust': 'thin',
	'price': 5.99,
	# Using a nested list so we can have more than one value inside the key value pair
	'ingredients': ['tomato sauce', 'cheese', 'pepperoni'],
	'custom toppings': []
}
print("Printing standard pepperoni pizza.")
for key in peperoni_pizza.keys():
	if key != 'ingredients' and key != 'custom toppings':
		print(key.title() + ":" + str(peperoni_pizza.get(key)))
	else:
		print(key.title() + ":")
		for i in range(len(peperoni_pizza.get(key))):
			print("\t* " + peperoni_pizza.get(key)[i])

print("Adding some custom toppings.")
peperoni_pizza.get('custom toppings').append('extra cheese')
peperoni_pizza.get('custom toppings').append('extra peperoni')

print("Printing customised pepperoni pizza.")
for key in peperoni_pizza.keys():
	if key != 'ingredients' and  key != 'custom toppings':
		print(key.title() + ":" + str(peperoni_pizza.get(key)))
	else:
		print(key.title() + ":")
		for i in range(len(peperoni_pizza.get(key))):
			print("\t* " + peperoni_pizza.get(key)[i])