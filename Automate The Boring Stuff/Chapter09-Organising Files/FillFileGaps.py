import os, shutil, random
from pathlib import Path
from PrintMessages import print_debug, print_info, print_error, print_warning


def create_initial_files(path, amount, no_filename_gaps):
	print(path)
	if not check_folder_exists(path):
		if not Path.is_absolute(Path(path)):
			path = get_absolute_path(path)
		create_folder(path)
		change_folder(path)
	else:
		if not Path.is_absolute(Path(path)):
			path = get_absolute_path(path)
	print_info('create_files_even using\n' + str(path))
	prn = random.randint(1, 100)
	for i in range(1, amount + 1):
		filename_and_content = get_filename_and_content(str(path), i)
		filename = filename_and_content[1]
		content = filename_and_content[0]

		if no_filename_gaps:
			print_debug('create_files - No filename gaps.')
			print(content)
			write_file(filename, content)
		else:
			if prn >= 50:
				if i % 2 == 0:
					print_debug('create_files - Odd filename gaps.')
					print(content)
					write_file(filename, content)
			else:
				if i % 2 != 0:
					print_debug('create_files - Even filename gaps.')
					print(content)
					write_file(filename, content)


def get_filename_and_content(path, number):
	filename = 'tmp_file' + str(number)
	return ['Saved file at ' + path + '/' + filename, filename]


def write_file(filename, content):
	print_debug('write_file - ' + filename)
	current_file = open(filename, 'w')
	current_file.write(str(content))
	current_file.close()


def check_folder_exists(path):
	if not Path.is_absolute(Path(path)):
		path = get_absolute_path(path)
		print_debug('check_folder_exists - Converted to absolute path using')
		print(path)
	if Path.exists(Path(path)):
		return True
	else:
		return False


def create_folder(path):
	if Path.is_absolute(Path(path)):
		Path.mkdir(Path(path))
	else:
		path = get_absolute_path(path)
		Path.mkdir(path)
	print_debug('create_folder using')
	print(str(path))


def change_folder(path):
	if Path.is_absolute(Path(path)):
		os.chdir(path)
	else:
		path = get_absolute_path(path)
		os.chdir(str(path))
	print_debug('change_folder using')
	print(str(path))


def get_absolute_path(path):
	if Path.is_absolute(Path(path)):
		return path
	else:
		print_debug('get_absolute_path - Returning\n' + str(Path.cwd() / path))
		return runtime_path / path


def cleanup(path):
	if not Path.is_absolute(Path(path)):
		path = get_absolute_path(path)
	if check_folder_exists(path):
		print_info('cleanup - Deleting' + str(path))
		shutil.rmtree(path)
		return True
	else:
		print_error('cleanup - Supplied path doesn\'t exist.')
		print(path)
		return False


def fill_in_file_gaps_with_insert(path, number):
	if not Path.is_absolute(Path(path)):
		path = get_absolute_path(path)
	if not (check_folder_exists(path)):
		print_error('fill_in_file_gaps_with_insert - Supplied path doesn\'t exist.')
		print(path)
		return False
	path = get_absolute_path(path)
	files_found = []
	for folderName, subfolders, files in os.walk(str(path)):
		print('The current folder is ' + folderName)

		for subfolder in subfolders:
			print('There is a subfolder called ' + subfolder)

		for file in files:
			print('There is a file called ' + file)
			files_found.append(file)

	print(files_found)
	files_found.sort()
	print(files_found)
	for i in range(1, number + 1):
		filename_and_content = get_filename_and_content(str(path), i)
		filename = filename_and_content[1]
		content = filename_and_content[0]
		if filename not in files_found:
			write_file(filename, content)



def fill_in_file_gaps_with_reorder(path):
	return None


runtime_path = Path.cwd()
relative_path = 'fill'
absolute_path = get_absolute_path(relative_path)
#create_initial_files(absolute_path, 5)
create_initial_files(relative_path, 5, False)
#create_initial_files(absolute_path, 5, False)
#create_initial_files(absolute_path, 5, True)
fill_in_file_gaps_with_insert(relative_path, 5)
#fill_in_file_gaps_with_insert(absolute_path, 5)
cleanup(relative_path)
#cleanup(absolute_path)



