import re

us_phone_number = re.compile(r'(\d{3})-(\d{3}-\d{4})')

def is_us_phone_number(text):
	match = us_phone_number.search(text)
	matched = False
	if match:
		# matchObject.groups() returns a tuple, use the multi-assignment trick to pass them to variables.
		area_code, phone_number = match.groups()
		print('The area code is ' + area_code + ' & the number is ' + phone_number)

		matched = True
		# need + 1, so i will be less than last index + 1
		for i in range(match.lastindex + 1):
			print('Found with search() ' + match.group(i))

	match = us_phone_number.match(text)
	if match:
		matched = True
		for i in range(match.lastindex + 1):
			print('Found with match() ' + match.group(i))
	return matched

print('415-555-4242 is a US phone number?')
print(is_us_phone_number('415-555-4242'))
print('\nMoshi moshi is a US phone number?')
print(is_us_phone_number('Moshi moshi'))