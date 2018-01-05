# 0,0 is top left, 0,5 is top right
# 8,0 is bottom left, 8,5 is bottom right
grid = [['.', '.', '.', '.', '.', '.'],
		['.', 'O', 'O', '.', '.', '.'],
		['O', 'O', 'O', 'O', '.', '.'],
		['O', 'O', 'O', 'O', 'O', '.'],
		['.', 'O', 'O', 'O', 'O', 'O'],
		['O', 'O', 'O', 'O', 'O', '.'],
		['O', 'O', 'O', 'O', '.', '.'],
		['.', 'O', 'O', '.', '.', '.'],
		['.', '.', '.', '.', '.', '.']]

# 9 rows x 6 column table
print('Rows:\t\t' + str(len(grid)))  # 9 deep
print('Columns:\t' + str(len(grid[1])) + '\n')  # 6 across

# @@@ PRINT PICTURE AS IS @@@
# i starts at 0, increments by 1 until the entire array is traversed
print('@@@ PRINT PICTURE AS IS @@@\n')
for i in range(len(grid)):
	output = ''
	# j starts at 0, increments by 1 until the end of the nested array (6)
	for j in range(len(grid[i])):
		# grab the value from the 2D array
		output += grid[i][j]
	# add a new line each time the loop is over
	output += '\n'
	print(output)
print('\n')

# @@@ ROTATE PICTURE 90 DEGREES TO THE RIGHT @@@
# ### First attempt ###
print('@@@ ROTATE PICTURE 90 DEGREES TO THE RIGHT @@@\n')
# i starts at 0, increments by 1 until the end of the nested array (6)
for i in range(len(grid[1])):
	output = ''
	# j starts at 8, decrements by 1, , until the start of the nested array (0)
	for j in range(8, -1, -1):
		# grab the value from the 2D array
		# output += 'j=' + str(j) + ' & i=' + str(i) + '. '
		output += grid[j][i]
	# add a new line each time the entire nested array is traversed
	output += '\n'
	print(output)
print('\n')

# ### Second Attempt ###
# i starts at 0, increments by 1, until the end of the nested array (6)
for i in range(len(grid[i])):
	output = ''
	# j is 0, increments by 1, until the end of the array (9)
	for j in range(len(grid)):
		# output += 'j=' + str(j) + ' & i=' + str(i) + '. '
		output += grid[j][i]
	output += '\n'
	print(output)
print('\n')

# @@@ ROTATE PICTURE 90 DEGREES TO THE LEFT @@@
# ### First attempt ###
print('@@@ ROTATE PICTURE 90 DEGREES TO THE LEFT @@@\n')
# i starts at 5, decrements by 1, until it hits 0
for i in range(5, -1, -1):
	output = ''
	# j starts at 0, increments by 1 until the end of the array
	for j in range(len(grid)):
		# grab the value from the 2D array
		# output += 'i=' + str(i) + ' & j=' + str(j) + '. '
		output += grid[j][i]
	# add a new line each time the entire nested array is traversed
	output += '\n'
	print(output)
print('\n')

# @@@ ROTATE PICTURE 180 DEGREES @@@
# ### FIRST ATTEMPT ###
print('@@@ ROTATE PICTURE 180 DEGREES @@@\n')
# i starts at 8, decrements by 1, until the start of the array (0)
for i in range(8, -1, -1):
	output = ''
	# j starts at 5, decrements by 1, until the start of the nested array (0)
	for j in range(5, -1, -1):
		#output += 'i=' + str(i) + ' & j=' + str(j) + '. '
		output += grid[i][j]
	output += '\n'
	print(output)
print('\n')
