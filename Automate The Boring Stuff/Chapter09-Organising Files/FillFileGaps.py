import os, shutil, random
from pathlib import Path
from PrintMessages import print_debug, print_info, print_error, print_warning


def create_initial_files(path, amount, no_filename_gaps):
	print(path)
	if not check_folder_exists(path):
		if not Path.is_absolute(Path(path)):
			path = get_absolute_path(path)
		create_folder(path)
	else:
		if not Path.is_absolute(Path(path)):
			path = get_absolute_path(path)
	print_info('create_files_even using\n' + str(path))
	change_folder(path)
	prn = random.randint(1, 100)
	for i in range(1, amount + 1):
		filename = get_filename(i)
		content = get_file_content(path, filename)

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


def get_filename(number):
	return 'tmp_file' + str(number)


def get_file_content(path, filename):
	return 'Saved file at ' + str(path) + '/' + str(filename)


def write_file(filename, content):
	print_debug('write_file - ' + filename)
	current_file = open(filename, 'w')
	current_file.write(str(content))
	current_file.close()


def check_folder_exists(path):
	if not Path.is_absolute(Path(path)):
		path = get_absolute_path(path)
		print_debug('check_folder_exists - Converted to absolute path using')
	if Path.exists(Path(path)):
		return True
	else:
		return False


def create_folder(path):
	if check_folder_exists(path):
		print_warning('create_folder - Folder already exists, nothing done. ')
	else:
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


def remove_file_gaps(path, number, use_insert):
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
	i = 1
	while i < number + 1:
		filename = get_filename(i)
		content = get_file_content(path, filename)
		if filename not in files_found and use_insert:
			write_file(filename, content)
			i += 1
			# else:
			# 	new_filename = get_filename(i - 1)
			# 	if Path.exists(path / filename):
			# 		print('Reorder goes here as ' + filename + ' not found.')
			# 		print('Rename ' + filename + ' to ' + new_filename)
			# 		#Path(path / filename).rename(new_filename)
			# 		i -= i
		else:
			i += 1



runtime_path = Path.cwd()
relative_path = 'fill'
absolute_path = get_absolute_path(relative_path)
#create_initial_files(absolute_path, 5)
create_initial_files(relative_path, 5, False)
#create_initial_files(absolute_path, 5, False)
#create_initial_files(absolute_path, 5, True)
#remove_file_gaps(relative_path, 5, True)
remove_file_gaps(absolute_path, 5, True)
#cleanup(relative_path)
#cleanup(absolute_path)



