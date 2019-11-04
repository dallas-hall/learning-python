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

reply = ""
print("You must be taller than 120cm to go in this ride.")
while True:
	reply = input("How tall are you? ")
	if reply.isdigit():
		reply = int(reply)
		break

if int(reply) >= 120:
	print(f"Great, {reply} cm is tall enough to ride.")
else:
	print(f"Sorry, {reply} cm isn't  tall enough to ride.")
