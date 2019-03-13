#!/bin/python3
# The pyw extension means that there won't be a terminal window shown.

'''
shelve = save to and read from a file
pypyerclip = clipboard copying and pasting
sys = command line arguments
'''
import shelve, pyperclip, sys

# mcb = multi-clipboard
mcbShelf = shelve.open('mcb')

# check that we have 3 arguments and the 1st argument is save
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	# save the clipboard contents
	mcbShelf[sys.argv[2]] = pyperclip.paste()
# if
elif len(sys.argv) == 2:
	# copy the list of keywords to the clipboard
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	# copy the contents into the clipboard
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

