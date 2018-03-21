# Create the nested dictionary (map) data structure containing people and the items they brought
allGuests = {
	'alice': {'apples': 5, 'pretzels': 12}
	, 'bob': {'ham sandwiches': 3, 'apples': 2}
	, 'carol': {'cups': 3, 'apple pies': 2}
}

# Create the list data structure containing all possible items to be brought
items = ['coffee scroll', 'pretzels', 'apples', 'ham sandwiches', 'cups', 'apple pies', 'chocolate']


def totalBrought(guests, item):
	numberBrought = 0
	# The guest's name is k & the dictionary containing items is v
	for k, v in guests.items():
		# use get() to get the item name using the passed argument, if it doesn't exist assign 0
		numberBrought = numberBrought + v.get(item, 0)
	return numberBrought


print("Number of items brought")
# Loop through all items and display the output
for i in range(len(items)):
	print(items[i] + ' ' + str(totalBrought(allGuests, items[i])))
