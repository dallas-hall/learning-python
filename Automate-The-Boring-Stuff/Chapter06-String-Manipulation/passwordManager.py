#! python3
'''
This is an insecure password manager.
'''

import sys, pyperclip

PASSWORDS = {'email': '0123456789ABCDEF'
			 ,'blog': 'P@ssword'
			 ,'luggage': '12345'}

# command line arguments are stored in sys.argv
if len(sys.argv) < 2:
	print('Usage: account-name - copy password')
	sys.exit()

# read in the account name
account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
	print('Pasting the password.')
	pyperclip.paste()
else:
	print('There is no account named ' + account)