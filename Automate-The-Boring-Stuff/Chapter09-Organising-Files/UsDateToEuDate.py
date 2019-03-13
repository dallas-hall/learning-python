#!/bin/python
import shutil, os, re, random
from pathlib import Path
words = ['eggs', 'spam', 'ham', 'milo', 'sausages', 'coffee', 'butter', 'toast']
extensions = ['.txt', '.php', '.java', '.js', '.py', '.c', '.cpp']


# Create a function for printing info messages
def print_info(message):
	print('[INFO] ' + str(message))


# Create a random date using American format. Date isn't necessarily valid.
def get_us_date():
	month = random.randint(1, 12)
	if month < 10:
		month = str(0) + str(month)
	day = random.randint(1, 31)
	if day < 10:
		day = str(0) + str(day)
	century = random.randint(19, 20)
	year = random.randint(0, 99)
	if year < 10:
		year = str(0) + str(year)
	return str(month) + '-' + str(day) + '-' + str(century) + str(year)


# Return a random word from a list of words.
def get_random_word():
	return str(words[random.randint(0, len(words) - 1)])


# Return a random extension
def get_random_extension():
	prn = random.randint(0, 99)
	if prn < 74:
		return str(extensions[random.randint(0, len(extensions) - 1)])
	else:
		return str('')


# Walk a path in the filesystem
def walk_and_print_path(path_to_walk):
	if not Path.exists(Path(path_to_walk)):
		print("The supplied path doesn't exist.")
	else:
		print_info('Walking the filesystem tree.')
		for folderName, subfolders, files in os.walk(str(path_to_walk)):
			print('The current folder is:\n' + folderName)
			for subfolder in subfolders:
				print('There is a subfolder called ' + subfolder)
			for file in files:
				print('There is a file called ' + file)


# Create a directory with some file to parse
print_info('Creating date files for parsing.')
path = os.getcwd() + '/date_files/'
if not os.path.exists(path):
	os.mkdir(path)
os.chdir(path)
print(os.getcwd())

# Create some files to parse.
print_info('Creating files.')
for i in range(10):
	filename = get_random_word() + get_us_date() + get_random_word() + get_random_extension()
	file = open(filename, 'w')
	file.write(filename)
	file.close()

walk_and_print_path(path)

# Use re.VERBOSE to create a regular expression across multiple lines with comments.
# ?: is a non-capturing group
usDate = re.compile(r"""^(.*?) # Match any text before the date
	((?:0|1)?\d)-? # Match the month digit(s) followed by an optional hyphen 
	((?:0|1|2|3)?\d)-? # Match the day digit(s) followed by an optional hyphen
	((?:19|20)?\d\d) # Match the year digits.
	(.*?)$ # Match any text after the date.
	""", re.VERBOSE)

# Loop through files, extract the date, and update the filename.
print_info('Renaming files.')
file_list = os.listdir(path)
for i in range(len(file_list)):
	current_filename = file_list[i]
	match_object = usDate.search(current_filename)

	# check if a date is present
	if match_object:
		initial_text = match_object.group(1)
		month = match_object.group(2)
		day = match_object.group(3)
		year = match_object.group(4)
		final_text = match_object.group(5)
		new_filename = initial_text + year + '-' + month + '-' + day + final_text
		print('Renaming %s to %s' %(current_filename, new_filename))
		Path.rename(Path(path + '/' + current_filename), Path(path + '/' + new_filename))
	else:
		continue

walk_and_print_path(path)
print_info('Deleting path and content.')
shutil.rmtree(path)
