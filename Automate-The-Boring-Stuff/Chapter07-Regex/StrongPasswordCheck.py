import re

lowercase = re.compile(r'[a-z]')
uppercase = re.compile(r'[A-Z]')
digits = re.compile(r'\d')

print('Input a password:')
password = input()

has_lowercase = lowercase.search(password)
has_uppercase = uppercase.search(password)
has_digit = digits.search(password)
password_length = len(password)

if has_lowercase and has_uppercase and has_digit and password_length >= 8:
	print('The password is strong.')
else:
	print('Your password sux.')

