#!/bin/python
import shutil, os, re
from pathlib import Path
from PrintMessages import print_info, print_error, print_warning, print_debug
debugging = True


def copy_file(source_path, target_path):
	shutil.copy(source_path, target_path)


def convert_relative_to_absolute(path_to_convert):
	if Path.exists(Path(path_to_convert)):
		if not Path.is_absolute(Path(path_to_convert)):
			print_info('Converting to absolute based on the current working directory.')
			new_path = Path.cwd() / Path(path_to_convert)
			return new_path
		else:
			print_warning('Path is already absolute.')
			return path_to_convert
	else:
		print_warning("Path doesn't exist. Do you wish to create it under the current working directory? Y|N")
		answer = input()
		if answer.lower() == 'y':
			print_info('Creating path.')
			Path.mkdir(Path.cwd() / Path(path_to_convert))
			return Path.cwd() / Path(path_to_convert)
		else:
			print_error('Cannot continue without a valid path, program terminating.')
			exit(1)


print('Enter the file pattern that you want to copy.')
file_pattern = input()
print('Enter the relative or absolute path where you want to copy from.')
source_path = input()
print('Enter the relative or absolute path where you want to copy to.')
target_path = input()
if debugging:
	print_debug('Printing original input contents.')
	print(file_pattern)
	print(source_path)
	print(target_path)

file_pattern = re.compile(r'' + file_pattern)
source_path = convert_relative_to_absolute(source_path)
target_path = convert_relative_to_absolute(target_path)
if debugging:
	print_debug('Printing updated input contents.')
	print(file_pattern.pattern)
	print(source_path)
	print(target_path)

print_info("Copying files matching '" + str(file_pattern) + "' from\n" + str(source_path) + "\nto\n" + str(target_path) +"\n")
for folderName, subfolders, files in os.walk(str(source_path)):
	for file in files:
		if file_pattern.search(file):
			print('Copying\n%s\nto\n%s' %(source_path / file, target_path))
			shutil.copy(source_path / file, target_path)
