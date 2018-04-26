import re

# Use a capture group and or logic to search for a specific hero ending with man. Only the first is matched.
regex = re.compile(r'(Bat|Super|Spider)man')
print('@@@ match() @@@\nThis will only return a match if the start of the string matches the expression.')
match = regex.match("Batman, Superman & Spiderman walk into a bar...")
print(match.group() + ' says to barman...')
match = regex.match("Superman, Batman & Spiderman walk into a bar...")
print(match.group() + ' says to barman...')
match = regex.match("Spiderman, Superman & Batman walk into a bar...")
print(match.group() + ' says to barman...')

print('\n@@@ search() @@@\nThis will only return the first match of the pattern within the entire string.')
match = regex.search("Batman, Superman & Spiderman walk into a bar...")
print(match.group() + ' says to barman...')
match = regex.search("Superman, Batman & Spiderman walk into a bar...")
print(match.group() + ' says to barman...')
match = regex.search("Spiderman, Superman & Batman walk into a bar...")
print(match.group() + ' says to barman...')
