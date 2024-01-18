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

users = []

if not users:
	print('Why are there no users?')

users = ['Alice', 'Bob', 'Charlie', 'David']
for user in users:
	if user == 'Alice':
		print('Alice? Alice? Who the fuck is Alice?')
	elif user == 'Bob':
		print('Why are you doing this, Bobby?')
	else:
		print(user)

print("Does Alice == alice? " + str(users[0] == 'alice'))
print("Does Alice.lower() == alice? " + str(users[0].lower() == 'alice'))
print("Does Alice != alice? " + str(users[0] != 'alice'))
print("Does Alice == Alice? " + str(users[0] == 'Alice'))

numbers = [1, 2]
print("Is 1 == 2? " + str(1 == 2))
print("Is 1 != 2? " + str(1 != 2))
print("Is 1 >= 2? " + str(1 >= 2))
print("Is 1 > 2? " + str(1 > 2))
print("Is 1 <= 2? " + str(1 <= 2))
print("Is 1 < 2? " + str(1 < 2))

