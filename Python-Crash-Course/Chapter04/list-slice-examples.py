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

# A list of 1 to 10
digits = list(range(1, 11))
print(digits)
print("The min is " + str(min(digits)))
print("The max is " + str(max(digits)))
print("The sum is " + str(sum(digits)))

print("Printing the first half and second half slices of the list.")
# Must do integer division
# Leaving out the first part of the slice starts from the beginning
print(digits[:len(digits) // 2])
# Leaving out the second part of the slice finishes at the end
print(digits[len(digits) // 2:])
print("Printing the last 3 items.")
print(digits[-3:])
print("Print every second item of the first half of the list.")
print(digits[:len(digits) // 2:2])
print("Print every second item of the last half of the list.")
print(digits[len(digits) // 2::2])

print("Using a slice in a for loop")
for n in digits[:len(digits) // 2]:
	print(n)

print("Copying the entire list via a slice [:]")
new_digits = digits[:]
for i in range(len(digits)):
	digits[i] = digits[i] * 2
	print(digits[i])
