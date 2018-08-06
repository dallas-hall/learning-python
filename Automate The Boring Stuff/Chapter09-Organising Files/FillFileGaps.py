import os
from PrintMessages import print_debug, print_info, print_error, print_warning


def create_files_full(path, amount):
	for i in range(1, amount + 1):
		filename = 'tmp_file' + str(i)
		print_debug('FULL' + path + '/' + filename)
		# current_file = open(path, 'w')
		# current_file.write(path)
		# current_file.close()


def create_files_even(path, amount):
	for i in range(1, amount + 1):
		if i % 2 == 0:
			filename = 'tmp_file' + str(i)
			print_debug('EVEN ' + path + '/' + filename)
			# current_file = open(path, 'w')
			# current_file.write(path)
			# current_file.close()


def create_files_odd(path, amount):
	for i in range(1, amount + 1):
		if i % 2 != 0:
			filename = 'tmp_file' + str(i)
			print_debug('ODD ' + path + '/' + filename)
			# current_file = open(path, 'w')
			# current_file.write(path)
			# current_file.close()


create_files_full('fill', 5)
create_files_even('fill', 5)
create_files_odd('fill', 5)


