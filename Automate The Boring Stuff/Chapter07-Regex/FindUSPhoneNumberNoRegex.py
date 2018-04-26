def is_us_phone_number(text):
	if len(text) != 12:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	return True

def has_us_phone_number(text):
	print('\nSearching text for US phone numbers.')
	for i in range(len(text)):
		chunk = text[i:i + 12]
		if is_us_phone_number(chunk):
			print('US Phone number found: ' + chunk)
	print('Done.')

print('415-555-4242 is a phone number:')
print(is_us_phone_number('415-555-4242'))
print('Moshi moshi is a phone number:')
print(is_us_phone_number('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
has_us_phone_number(message)