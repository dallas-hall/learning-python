def print_table(a_list_of_lists):
	longest_string = 0;
	for i in range(len(a_list_of_lists)):
		for j in range(len(a_list_of_lists[i])):
			if len(a_list_of_lists[i][j]) > longest_string:
				longest_string = len(a_list_of_lists[i][j])
	print('Longest string is: ' + str(longest_string))

	print('The formatted list is: ')
	for i in range(len(a_list_of_lists)):
		current_line = ''
		for j in range(len(a_list_of_lists[i])):
			current_line += a_list_of_lists[i][j].rjust(longest_string, '*') + ' '
		print(current_line)


start_list = [
	['string 1', 'string 2', 'string 3']
	,['string 10', 'string 20', 'string 30']
	,['string 100', 'string 200', 'string 300']
]

print('The starting list is: ' + str(start_list))
print_table(start_list)


