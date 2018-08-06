import os, shutil
from pathlib import Path
from PrintMessages import print_debug, print_info, print_error, print_warning


def create_files_full(path, amount):
	if not check_folder_exists(path):
		create_folder(path)
		change_folder(path)
	path = get_absolute_path(path)
	print_info('Creating FULL files at:\n' + path)
	for i in range(1, amount + 1):
		filename = 'tmp_file' + str(i)
		print_debug('FULL' + path + '/' + filename)
		current_file = open(filename, 'w')
		current_file.write(path + '/' + filename)
		current_file.close()


def create_files_even(path, amount):
	if not check_folder_exists(path):
		create_folder(path)
		change_folder(path)
	path = get_absolute_path(path)
	print_info('Creating EVEN files at:\n' + path)
	for i in range(1, amount + 1):
		if i % 2 == 0:
			filename = 'tmp_file' + str(i)
			print_debug('EVEN ' + path + '/' + filename)
			current_file = open(filename, 'w')
			current_file.write(path + '/' + filename)
			current_file.close()


def create_files_odd(path, amount):
	if not check_folder_exists(path):
		create_folder(path)
		change_folder(path)
	path = get_absolute_path(path)
	print_info('Creating ODD files at:\n' + path)
	for i in range(1, amount + 1):
		if i % 2 != 0:
			filename = 'tmp_file' + str(i)
			print_debug('ODD ' + path + '/' + filename)
			current_file = open(filename, 'w')
			current_file.write(path + '/' + filename)
			current_file.close()


def check_folder_exists(path):
	if Path.exists(Path(path)):
		return True
	else:
		return False


def create_folder(path):
	Path.mkdir(Path(path))


def change_folder(path):
	if Path.is_absolute(Path(path)):
		os.chdir(path)
	else:
		os.chdir(os.getcwd() + '/' + path)


def get_absolute_path(path):
	if Path.is_absolute(Path(path)):
		return path
	else:
		return os.getcwd() + '/' + path


def cleanup(path):
	if not Path.is_absolute(Path(path)):
		print_error("Supplied path must be absolute.")
		return False
	if check_folder_exists(path):
		print_info('Deleting:\n' + path)
		shutil.rmtree(path)
		return True
	else:
		return False


relative_path = 'fill'
absolute_path = os.getcwd() + '/' + relative_path
#create_files_full(absolute_path, 5)
create_files_even(relative_path, 5)
#create_files_odd(relative_path, 5)
cleanup(relative_path)
cleanup(absolute_path)



