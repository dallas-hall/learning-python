# create a list
catNames = []

# loop until users ends
while True:
	# ask the user for input
	print('Enter the name of cat number ' + str(len(catNames) + 1)
		  + '\nOr enter EXIT to exit the program.')
	# store the input
	name = input()
	# process the input
	if name == 'EXIT':
		break
	# perform list concatenation after converting from string to list
	catNames = catNames + [str(name)]

# print the list
print('The cats names are:')
for name in catNames:
	print(name + ' ')
