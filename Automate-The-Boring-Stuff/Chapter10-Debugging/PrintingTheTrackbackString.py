import traceback
error_filename = 'error_file.txt'

try:
	raise Exception('An error message.')
except:
	error_file = open(error_filename, 'w')
	error_file.write(traceback.format_exc())
	error_file.close()
	print('The tracebook string was written out to the file ' + error_filename)

