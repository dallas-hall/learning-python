import re

us_phone_number = re.compile(r'(\d{3})-(\d{3}-\d{4})')

def is_us_phone_number(text):
	match = us_phone_number.search(text)
	matched = False
	if match:
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

print('415-555-4242 is a phone number?')
print(is_us_phone_number('415-555-4242'))
print('Moshi moshi is a phone number?')
print(is_us_phone_number('Moshi moshi'))