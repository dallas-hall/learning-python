#!/bin/python
import shutil, os, re, random
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


# Create a directory with some file to parse
print_info('Creating date files for parsing.')
path = os.getcwd() + '/date_files/'
if not os.path.exists(path):
	os.mkdir(path)
os.chdir(path)
print(os.getcwd())

# Create some files to parse.

for i in range(10):
	filename = get_random_word() + get_us_date() + get_random_word() + get_random_extension()
	print_info('Creating file ' + filename)
	file = open(filename, 'w')
	file.write(filename)
	file.close()


# Use re.VERBOSE to create a regular expression across multiple lines with comments.
usDate = re.compile(r"""^(.*?) # Match any text before the date
	((0|1)?\d)-? # Match the month digit(s) followed by an optional hyphen 
	((0|1|2|3)?\d)-? # Match the day digit(s) followed by an optional hyphen
	((19|20)?\d\d) # Match the year digits.
	(.*?)$ # Match any text after the date.
	""", re.VERBOSE)

print_info('Deleting path and content.')
shutil.rmtree(path)
