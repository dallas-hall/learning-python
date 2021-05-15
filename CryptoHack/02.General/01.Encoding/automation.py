#!/usr/bin/env python3

# FIFTH CHALLENGE

# Now you've got the hang of the various encodings you'll be encountering, let's have a look at automating it.
# Can you pass all 100 levels to get the flag?
# The 13377.py file attached below is the source code for what's running on the server. The pwntools_example.py file provides the start of a solution using the incredibly convenient pwntools library. which you can use if you like. pwntools however is incompatible with Windows, so telnetlib_example.py is also provided.
# For more information about connecting to interactive challenges, see the FAQ. Feel free to skip ahead to the cryptography if you aren't in the mood for a coding challenge!
# Connect at nc socket.cryptohack.org 13377

# https://docs.python.org/3/library/base64.html#module-base64
# https://docs.python.org/3/library/binascii.html
# https://stackoverflow.com/a/3270252 & https://docs.python.org/3/library/codecs.html#text-transforms
import codecs
import json

# https://pycryptodome.readthedocs.io/en/latest/
from Crypto.Util.number import long_to_bytes
# Taken from  pwntools.py - https://docs.pwntools.com/en/latest/
from pwn import *

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

r = remote('socket.cryptohack.org', 13377, level='debug')
level = 1


def json_recv():
	line = r.recvline()
	return json.loads(line.decode())


def json_send(hsh):
	request = json.dumps(hsh).encode()
	r.sendline(request)


while level <= 100:
	print('[INFO] Level ' + str(level))
	# Get JSON response
	received = json_recv()
	print("Received type: ")
	print(received["type"])
	print("Received encoded value: ")
	print(received["encoded"])

	# Process response
	flag = ''
	if received["type"] == "base64":
		# # https://docs.python.org/3/library/base64.html#base64.b64decode
		flag = base64.b64decode(received['encoded'])
	elif received["type"] == "hex":
		# https://docs.python.org/3/library/binascii.html#binascii.unhexlify
		# https://docs.python.org/3/library/stdtypes.html#bytes.decode
		flag = binascii.unhexlify(received['encoded'])
	elif received["type"] == "rot13":
		flag = codecs.decode(received['encoded'], 'rot_13')
	elif received["type"] == "bigint":
		# Ignore the 0x in the string and convert to an int - https://docs.python.org/3/library/functions.html#int
		long = int(received['encoded'], 16)
		flag = long_to_bytes(long)
	elif received["type"] == "utf-8":
		for i in range(len(received['encoded'])):
			flag += chr(received['encoded'][i])
	print(flag)

	# Check if the flag is still binary - https://stackoverflow.com/a/34870210
	try:
		flag = flag.decode()
	except (UnicodeDecodeError, AttributeError):
		pass

	print('Post binary decode: ' + flag)
	# Send processed response
	to_send = {
		"decoded": flag
	}

	json_send(to_send)

	level += 1

# Get the flag after 100 rounds
json_recv()
