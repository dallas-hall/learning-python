#!/usr/bin/python3
import logging, sys, os, time
from user import User
from getpass import getpass

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

username = input("Hello, please enter your username: ")
password = getpass("Password: ")
email = input("Email: ")

new_user = User(username, password, email)

absolute_file_path = "/media/veracrypt1/Development/io-files/users.txt"
delimiter = ","
with open(absolute_file_path, "a") as file_object:
	file_object.write(new_user.get_name() + delimiter)
	file_object.write(new_user.get_password() + delimiter)
	file_object.write(new_user.get_email() + delimiter)
	file_object.write(new_user.get_join_date() + "\n")

