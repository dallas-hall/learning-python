# create a dictionary
birthdays = {'Alice': '1981-01-01', 'Bob': '1980-12-12'}

while True:
	# get user input
	print('Enter a name or type exit to exit')
	# store user input
	name = input()
	print(name)
	# check if exiting
	if name == '':
		break

	if name in birthdays:
		print(birthdays[name] + ' is teh birthday of ' + name)
	else:
		print('No person found.\nEnter the person''s birthday')
		birthday = input()
		birthdays[name] = birthday
		print('Birthdays database updated.')
