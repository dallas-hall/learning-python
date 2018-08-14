def okay():
	error()


def error():
	raise Exception('This will print out the call stack information and source code information.')


okay()