#!/usr/bin/python3

def printBox(symbol, width, height):
	# Check input
	if len(symbol) != 1:
		raise Exception('Symbol must be only 1 character long.')
	if width <= 2:
		raise Exception('Width must be greater than 2.')
	if height <= 2:
		raise Exception('Height must be greater than 2.')
	# Printer box header
	print(symbol * width)
	# Print box sides
	for i in range(height - 2):
		print(symbol + (' ' * (width - 2)) + symbol)
	# Print box footer
	print(symbol * width)


for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
	try:
		printBox(sym, w, h)
	except Exception as e:
		print('An Exception occurred: ' + str(e))