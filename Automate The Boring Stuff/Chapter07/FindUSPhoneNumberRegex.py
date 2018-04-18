import re

us_phone_number = re.compile(r'\d{3}-\d{3}-\d{4}')

def is_us_phone_number(text):
	match = us_phone_number.search(text)
	if match:
		print('Found with search() ' + match.group())
	match = us_phone_number.match(text)
	if match:
		print('Found with match() ' + match.group())

def has_us_phone_number(text):
	print('\nSearching text for US phone numbers.')
	for i in range(len(text)):
		chunk = text[i:i + 12]
		is_us_phone_number(chunk)
	print('Done.')

print('415-555-4242 is a phone number:')
print(is_us_phone_number('415-555-4242'))
print('Moshi moshi is a phone number:')
print(is_us_phone_number('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
has_us_phone_number(message)