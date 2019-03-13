print('@@@ try / except inside the function @@@')


def spam(divideBy):
	# try running some code, if there is an error go to the except
	try:
		return 42 / divideBy
	# process the error(s) defined here
	except ZeroDivisionError:
		print('Error: Cannot divide by 0')


print(spam(0))
print(spam(1))
print(spam(2))
print(spam(4))

print('@@@ try / except wrapping the code @@@')


def spam(divideBy):
	return 42 / divideBy


try:
	print(spam(0))
	# code below here is never executed because of the error above
	print(spam(1))
	print(spam(2))
	print(spam(4))
except ZeroDivisionError:
	print('Error: Cannot divide by 0')
