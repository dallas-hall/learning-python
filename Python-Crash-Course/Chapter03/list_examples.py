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

print("# List Item Manipulations")

# Create a list
items = ['bag', 'gold', 'cloak', 'staff', 'shield']

print(items)
print("First item is '" + items[0].title() + "'")
print("Last item is '" + items[-1].title() + "'")

print("Replace an item.")
items[1] = ''
print(items)
print("Remove an item by its value.")
# Only removes the first instance.
items.remove('')
print(items)
# Use this when you don't care for the value you deleted.
print("Delete the last value.")
del items[-1]
print(items)

print("Append a value.")
items.append('silver')
print(items)

print("Delete all items.")
items.clear()
print(items)
items = ['bag', 'gold', 'cloak', 'staff', 'shield']
print(items)
items = []
print(items)

print("Insert an item")
items = ['bag', 'gold', 'cloak', 'staff', 'shield']
items.insert(1, "silver")
print(items)

# Use this when you want to use the value after removing it.
print("Pop an item off the list, be default the last item.")
popped_item = items.pop()
print(popped_item)
print(items)
print("Pop an item off the list using an index.")
popped_item = items.pop(0)
print(popped_item)
print(items)

print("\n# List Sorting")
print("Resetting the list.")
items = ['bag', 'gold', 'cloak', 'staff', 'shield']
print(items)
print("Sorting the list temporarily (alphabetical).")
print(sorted(items))
print("Sorting the list temporarily (reversed alphabetical).")
print(sorted(items, reverse=True))
print(items)
print("Reverse the list permanently.")
items.reverse()
print(items)
print("Reverse the list permanently for the second time, back to the original order.")
items.reverse()
print(items)
print("Sorting the list permanently (alphabetical).")
items.sort()
print(items)
print("Sorting the list permanently (reversed alphabetical).")
items.sort(reverse=True)
print(items)
print("The length of the list is " + str(len(items)))
