import os, shutil
from pathlib import Path
from PrintMessages import print_debug, print_info, print_error, print_warning


def create_files_full(path, amount):
	if not check_folder(path):
		create_folder(path)
		os.chdir(os.getcwd() + '/' + path)
	for i in range(1, amount + 1):
		filename = 'tmp_file' + str(i)
		print_debug('FULL' + path + '/' + filename)
		current_file = open(filename, 'w')
		current_file.write(path + '/' + filename)
		current_file.close()


def create_files_even(path, amount):
	if not check_folder(path):
		create_folder(path)
		os.chdir(os.getcwd() + '/' + path)
	for i in range(1, amount + 1):
		if i % 2 == 0:
			filename = 'tmp_file' + str(i)
			print_debug('EVEN ' + path + '/' + filename)
			current_file = open(filename, 'w')
			current_file.write(path + '/' + filename)
			current_file.close()


def create_files_odd(path, amount):
	if not check_folder(path):
		create_folder(path)
		os.chdir(os.getcwd() + '/' + path)
	for i in range(1, amount + 1):
		if i % 2 != 0:
			filename = 'tmp_file' + str(i)
			print_debug('ODD ' + path + '/' + filename)
			current_file = open(filename, 'w')
			current_file.write(path + '/' + filename)
			current_file.close()


def check_folder(path):
	if Path.exists(Path(path)):
		return True
	else:
		return False


def create_folder(path):
	Path.mkdir(Path(path))


def cleanup(path):
	if check_folder(path):
		shutil.rmtree(path)
		return True
	else:
		return False


#create_files_full('fill', 5)
create_files_even('fill', 5)
#create_files_odd('fill', 5)


