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

# Handle the exception object
n = input("Enter an integer: ")
m = input("Enter an integer: ")

try:
	answer = int(n) / int(m)
except ZeroDivisionError:
	print("Cannot divide by 0.")
except ValueError:
	print("You entered an invalid character.")
else:
	print(f"{n} / {m} is {answer}")
