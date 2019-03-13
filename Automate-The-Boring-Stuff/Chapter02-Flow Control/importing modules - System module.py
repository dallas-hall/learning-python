# import the sys module
import sys

# infinite loop
while True:
	# print a message
	print('Type exit to exit.')
	# accept user input
	response = input()
	# test user input
	if response == 'exit':
		# if user input matches the test, exit the program
		sys.exit()
	# print back user input
	print('You have typed ' + response + '.')
