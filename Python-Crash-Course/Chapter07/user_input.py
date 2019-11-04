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

# input accepts a parameter to print as a message.
reply = input("What is your favourite colour? ")
print(f"Really? You like {reply}? That colour is stupid.")

prompt = "Never tell anyone your credit number."
# += concatenates a string to a string
prompt += "\nWhat is your credit card number?"

reply = input(prompt)
print(f"You credit card number is {reply}.")


