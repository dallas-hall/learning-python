strings = ['8', '8.0', '8a', 'chars', '!@#', ' \t', 'Mr Jones']

# check if these strings are something
for i in range(len(strings)):
	print('The current value of strings[' + str(i) + '] is: \'' + str(strings[i]) + '\'')
	# checks for strings with a starting capital.
	print('Is variables[' + str(i) + '] a title? ' + str(strings[i].istitle()))
	# checks for strings with only letters
	print('Is variables[' + str(i) + '] alpha? ' + str(strings[i].isalpha()))
	# checks for strings containing numbers
	print('Is variables[' + str(i) + '] numeric? ' + str(strings[i].isnumeric()))
	print('Is variables[' + str(i) + '] a digit? ' + str(strings[i].isdigit()))
	print('Is variables[' + str(i) + '] a decimal? ' + str(strings[i].isdecimal()))
	# checks for strings containing alphas and or numbers
	print('Is variables[' + str(i) + '] alpha-numeric? ' + str(strings[i].isalnum()))
	# check if the string contains printable characters
	print('Is variables[' + str(i) + '] printable? ' + str(strings[i].isprintable()))
	# checks if the string has only whitespace characters
	print('Is variables[' + str(i) + '] whitespace chars only? ' + str(strings[i].isspace()))
	print()
