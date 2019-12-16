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

absolute_file_path = "/media/veracrypt1/Development/io-files/users.txt"
delimiter = ","


# Check if running for the first time, is yes, sign up, if no login
def load_users():
	try:
		# Read the file as utf-8
		with open(absolute_file_path, "r", encoding="utf-8") as file:
			contents = file.read()
	except FileNotFoundError:
		return None
	else:
		recreated_users = []
		with open(absolute_file_path, "r", encoding="utf-8") as file:
			all_users_csv = file.readlines()
			for user_csv in all_users_csv:
				user_list = user_csv.split(',')
				user = User(user_list[0], user_list[1], user_list[2], user_list[3])
				recreated_users.append(user)
		return recreated_users


def login(username):
	found = False
	for user in users:
		if user.get_name() == username:
			found = True
			password = getpass("Password: ")
			if user.get_password() == password:
				print(f"Welcome back, {user.get_name()}.")
			else:
				print("Incorrect password.")
	if not found:
		signup(username)


def signup(username):
	password = getpass("Password: ")
	email = input("Email: ")
	new_user = User(username, password, email)
	save_user(new_user)


def save_user(user):
	with open(absolute_file_path, "a", encoding="utf-8") as file:
		file.write(user.get_name() + delimiter)
		file.write(user.get_password() + delimiter)
		file.write(user.get_email() + delimiter)
		file.write(user.get_join_date() + "\n")


users = load_users()
username = input("Hello, please enter your username: ")
if users:
	login(username)
else:
	signup(username)
