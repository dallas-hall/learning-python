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

users = ['Alice', 'Bob']
for user in users:
	print(user)

print("Does Alice == alice? " + str(users[0] == 'alice'))
print("Does Alice != alice? " + str(users[0] != 'alice'))
print("Does Alice == Alice? " + str(users[0] == 'Alice'))

numbers = [1, 2]
print("Is 1 == 2? " + str(1 == 2))
print("Is 1 != 2? " + str(1 != 2))
print("Is 1 >= 2? " + str(1 >= 2))
print("Is 1 > 2? " + str(1 > 2))
print("Is 1 <= 2? " + str(1 <= 2))
print("Is 1 < 2? " + str(1 < 2))

