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

active = True

reply = ""
print("You must be taller than 120cm to ride the D.")
while active:
	reply = input("How tall are you in cm?\n")
	if reply.lower() == "exit" or reply.lower() == "quit":
		exit(0)
	elif reply.isdigit():
		reply = int(reply)
		active = False
	else:
		print('Invalid input, try again.')

if int(reply) >= 120:
	print(f"Great, {reply} cm is tall enough to ride the D.")
else:
	print(f"Sorry, {reply} cm isn't tall enough to ride the D.")
