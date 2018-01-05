def list_to_string(a_list):
	output = ''
	# loop through the entire list
	for i in range(len(a_list)):
		# all elements except last element
		if i != len(a_list) - 1:
			output += a_list[i] + ', '
		# the last element
		elif i == len(a_list) - 1:
			output += 'and ' + a_list[i] + '.'
	print(output)


spam = ['apples', 'bananas', 'tofu', 'cats']
list_to_string(spam)

spam = ['It is certain',
		'It is decidedly so',
		'Yes definitely',
		'Reply hazy try again',
		'Ask again later',
		'Concentrate and ask again',
		'My reply is no',
		'Outlook not so good',
		'Very doubtful']
list_to_string(spam)
