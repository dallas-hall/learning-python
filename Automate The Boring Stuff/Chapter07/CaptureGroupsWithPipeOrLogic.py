import re

# Use a capture group and or logic to search for a specific hero ending with man. Only the first is matched.
regex = re.compile(r'(Bat|Super|Spider)man')
match = regex.match("Batman, Superman & Spiderman walk into a bar...")
print(match.group() + ' says to barman...')
match = regex.match("Superman, Batman & Spiderman walk into a bar...")
print(match.group() + ' says to barman...')
match = regex.match("Spiderman, Superman & Batman walk into a bar...")
print(match.group() + ' says to barman...')