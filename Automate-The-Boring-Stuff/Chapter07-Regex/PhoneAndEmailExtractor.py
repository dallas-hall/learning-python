import re, pyperclip
'''
800-420-7240
415-863-9900
415-863-9950
02-12-345-678
02 12345678
(02) 12345678
info@nostarch.com
media@nostarch.com
academic@nostarch.com
help@nostarch.com
'''

usPhoneRegex = re.compile(r'''(
    ^(\d{3}|\(\d{3}\))?				# area code capture group
    (\s|-|\.)?						# separator capture group
    (\d{3})							# first 3 digits capture group
    (\s|-|\.)						# separator capture group
    (\d{4})                         # last 4 digits capture group
    (\s*(ext|x|ext.)\s*(\d{2,5}))?	# extension capture group
    )''', re.VERBOSE | re.MULTILINE)

auPhoneRegex = re.compile(r'''(
	^(\d{2}|\(\d{2}\))?				# area code capture group
	(\s|-|\.)?						# separator capture group
	(\d{2})							# a
	(\s|-|\.)?						# separator capture group
	(\d{3})							# b
	(\s|-|\.)?						# separator capture group
	(\d{3})							# c
    (\s*(ext|x|ext.)\s*(\d{2,5}))?	# extension capture group
	)''', re.VERBOSE | re.MULTILINE)

# https://www.regular-expressions.info/email.html
emailRegex = re.compile(r'''(
	\b								# start of the word block & capture group
	[A-Za-z0-9._%+-]+				# username
	@								# the @ symbol	
	[A-Za-z0-9.-]+\.[A-Za-z]{2,}	# the domain name
	\b								# end of the word block & capture group
	)''', re.VERBOSE)

search_text = str(pyperclip.paste())
matches = []
''' US Numbers
We only care about match groups 1, 3, and 5. This is because 1 will hold
the area code, 3 will hold the next 3 digits, and 5 will hold the final
4 digits.
'''
for groups in usPhoneRegex.findall(search_text):
	# Create a new list separated by a -
	phone_number = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phone_number = ' x' + groups[8]
	matches.append(phone_number)

''' AUS Numbers
We only care about match groups 1, 3, 5, and 7. This is because 1 will hold
the area code, 3 will hold the next 2 digits, and 5 and 7 will hold the final
6 digits.
'''
for groups in auPhoneRegex.findall(search_text):
	# Create a new list separated by a -
	phone_number = '-'.join([groups[1], groups[3], groups[5], groups[7]])
	matches.append(phone_number)

for groups in emailRegex.findall(search_text):
	matches.append(groups)

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')
