import webbrowser, sys, logging, pyperclip
# Parliament House, Canberra

# Define logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')

# Handle program arguments, each program argument will be stored in its own unique array element inside sys.argv
if len(sys.argv) > 1:
	# Use list slicing to get the entire array
	address = ' '.join(sys.argv[1:])
	logging.debug('This value of address is :\n' + address)
else:
	# Get address from the clipboard
	address = pyperclip.paste()

# Opens a tab in the default system browser
webbrowser.open('https://www.google.com/maps/place/' + address)