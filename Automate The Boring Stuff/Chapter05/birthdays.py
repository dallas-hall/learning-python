# create a dictionary
birthdays = {'Alice': '1981-01-01', 'Bob': '1980-12-12'}

while True:
	# get user input
	print('Enter a name or type exit to exit. The name is case sensitive.')
	# store user input
	name = input()
	print(name)
	# check if exiting
	if name.lower() == 'exit':
		break

	if name in birthdays:
		print(birthdays[name] + ' is teh birthday of ' + name)
	else:
		print('No person found.\nEnter the person''s birthday')
		birthday = input()
		birthdays[name] = birthday
		print('Birthdays database updated.')

print('Printing dictionary keys.')
for k in birthdays.keys():
	print(k)

print('Printing dictionary values.')
for v in birthdays.values():
	print(v)

print('Printing dictionary key and value pairs. Method 1')
for i in birthdays.items():
	print(i)

print('Printing dictionary key and value pairs. Method 2')
for k, v in birthdays.items():
	print(k + " " + v)

