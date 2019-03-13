import re

def regex_strip(input_string):
	start_spaces = re.compile(r'^\s+')
	end_spaces = re.compile(r'\s+$')
	new_string = end_spaces.sub('', start_spaces.sub('', input_string))
	return new_string

a_string = ' hi I am a string\t '
print('Starting string inside double quotes is: "' + a_string + '"')
print('Starting string inside double quotes after regex_strip() is: "' + regex_strip(a_string) + '"')

