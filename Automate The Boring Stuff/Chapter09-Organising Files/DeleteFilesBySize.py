#!/bin/bash
import subprocess, os, shutil, random
from PrintMessages import print_info, print_warning, print_debug, print_error
from pathlib import Path
debugging = True


def byte_conversion(file_size_in_bytes):
	if file_size_in_bytes < 1024:
		calculated_file_size = file_size_in_bytes
		calculated_file_size_unit = 'bytes'
	# 1024 * 1024 = 1048576
	elif file_size_in_bytes < 1048576:
		calculated_file_size = file_size_in_bytes / 1024
		calculated_file_size_unit = 'KiB'
	# 1024 * 1024 * 1024 = 1073741824
	elif file_size_in_bytes < 1073741824:
		calculated_file_size = file_size_in_bytes / 1024 / 1024
		calculated_file_size_unit = 'MiB'
	else:
		calculated_file_size = file_size_in_bytes / 1024 / 1024 / 1024
		calculated_file_size_unit = 'GiB'
	#print_debug('The current file called ' + file + ' has a size of ' + str(calculated_file_size) + ' ' + calculated_file_size_unit)
	return [calculated_file_size, calculated_file_size_unit]


def kib_to_byte(kib_amount):
	return int(kib_amount) * 1024


def mib_to_byte(mib_amount):
	return int(mib_amount) * 1024 * 1024


def gib_to_byte(gib_amount):
	return int(gib_amount) * 1024 * 1024 * 1024


print('Enter the path to work in.')
work_path = input()
if not Path.exists(Path.cwd() / work_path):
	print_warning("The supplied path doesn't exist, it is being created in the current working directory.")
	Path.mkdir(Path.cwd() / work_path)
	work_path = Path.cwd() / work_path
elif not Path.is_absolute(Path(work_path)):
	print_warning("The supplied path wasn't absolute, it is being converted using the current working directory.")
	work_path = Path.cwd() / work_path
print_info('Working with the path:\n' + str(work_path))

while True:
	print('Enter the file size unit b|k|m|g')
	print('This will use the binary prefix of 1024.')
	file_size_unit = input().upper()
	if file_size_unit != 'B' and file_size_unit != 'K' and file_size_unit != 'M' and file_size_unit != 'G':
		print_error('Incorrect file size unit.')
	else:
		break

while True:
	print('Enter the file size. Keep in mind your remaining disk space.')
	file_size = input()
	if not file_size.isdigit():
		print_error('Incorrect file size. Use integers only.')
	else:
		break


while True:
	print('Enter how many files to create.')
	number_to_allocate = input()
	if not number_to_allocate.isdigit():
		print_error('Incorrect amount. Use integers only.')
	else:
		break


if debugging:
	print_debug('The file size is ' + file_size)
	print_debug('The file size unit is ' + file_size_unit)
	print_debug('The amount of files to allocate space for is ' + number_to_allocate)

# Using fallocate to pre-allocate space for each file. https://stackoverflow.com/a/8706714
print_info('Allocating space.')
os.chdir(str(work_path))
if debugging:
	print_debug('Current path is:\n' + str(Path.cwd()))
size_units = ['B', 'K', 'M', 'G']
for i in range(int(number_to_allocate) * 2):
	# For every even number create a file of different size.
	if i % 2 == 0:
		random_size_unit = size_units[random.randint(0, len(size_units) - 1)]
		if random_size_unit != 'B':
			args = ['fallocate', '-l', str(1) + str(random_size_unit), 'pre-allocated_file' + str(i + 1)]
		else:
			args = ['fallocate', '-l', str(1), 'pre-allocated_file' + str(i + 1)]
	# https://docs.python.org/3/library/subprocess.html#subprocess.run
	else:
		if file_size_unit != 'B':
			args = ['fallocate', '-l', str(file_size) + str(file_size_unit), 'pre-allocated_file' + str(i + 1)]
		else:
			args = ['fallocate', '-l', str(file_size), 'pre-allocated_file' + str(i + 1)]

	if debugging:
		print_debug(str(args))
	subprocess.run(args)

print_info('Walking file system at:\n' + str(work_path))
for folderName, subfolders, files in os.walk(str(work_path)):
	print('The current folder is ' + folderName)
	for subfolder in subfolders:
		print('There is a subfolder called ' + subfolder)
	for file in files:
		current_file_size_bytes = os.path.getsize(file)
		byte_conversion(current_file_size_bytes)


while True:
	print('Enter file size threshold. All files greater than or equal to this will be deleted.\nNote that the previous file unit size will be used.')
	file_size_threshold = input()
	if not file_size_threshold.isdigit():
		print_error('Invalid input, enter integers only.')
	else:
		break

print_info('Deleting files greater than or equal to the supplied threshold of ' + file_size_threshold + ' ' + file_size_unit)
if file_size_unit == 'K':
	byte_threshold = kib_to_byte(file_size_threshold)
elif file_size_unit == 'M':
	byte_threshold = mib_to_byte(file_size_threshold)
elif file_size_unit == 'G':
	byte_threshold = gib_to_byte(file_size_threshold)
else:
	byte_threshold = file_size_threshold
print_debug(str(byte_threshold))
for folderName, subfolders, files in os.walk(str(work_path)):
	print('The current folder is ' + folderName)
	for subfolder in subfolders:
		print('There is a subfolder called ' + subfolder)
	for file in files:
		current_file_size_bytes = os.path.getsize(file)
		current_file_converted = byte_conversion(current_file_size_bytes)
		if current_file_size_bytes >= int(byte_threshold):
			print_debug('The file ' + file + ' sized ' + str(current_file_converted[0]) + ' ' + str(current_file_converted[1]) + ' will be deleted.\nBecause it is greater than or equal to ' + str(file_size_threshold) + ' ' + file_size_unit)
			Path.unlink(Path(file))

#print_info('Deleting root path and all files and folders of:\n' + str(work_path))
#shutil.rmtree(str(work_path))
