# create a list
myPets = ['Grubby', 'Tank Cat']

# get user input
print('Enter a pet name:')
name = input()

# process user input
if name not in myPets:
	print("I don't have a pet named " + name + '.')
else:
	print(name + ' is my pet.')
