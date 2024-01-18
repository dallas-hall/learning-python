#!/usr/bin/env python3
import logging, sys, os, time

# Had to mark Chapter09 folder as sources root.
from user import User
from getpass import getpass
from pathlib import Path

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.100)

path_2e = "/ssd/Development/random-files-for-dev-io/users-2e.txt"
path_3e = Path("/ssd/Development/random-files-for-dev-io/users-3e.txt")
delimiter = ","


# Check if running for the first time, is yes, sign up, if no login
def load_users(path, edition):
	if edition == 2:
		try:
			# Read the file as utf-8
			with open(path, "r", encoding="utf-8") as file:
				contents = file.read()
		except FileNotFoundError:
			return None
		else:
			recreated_users = []
			with open(path, "r", encoding="utf-8") as file:
				all_users_csv = file.readlines()
				for user_csv in all_users_csv:
					user_list = user_csv.split(',')
					user = User(user_list[0], user_list[1], user_list[2], user_list[3])
					recreated_users.append(user)
			return recreated_users
	elif edition == 3:
		try:
			contents = path.read_text(encoding="utf-8")
		except FileNotFoundError:
			return None
		else:
			recreated_users = []
			lines = contents.splitlines()
			for line in lines:
				user_list = line.split(',')
				user = User(user_list[0], user_list[1], user_list[2], user_list[3])
				recreated_users.append(user)
			return recreated_users


def login(uid, edition):
	found = False
	for user in users:
		if user.get_name() == uid:
			found = True
			password = getpass(f"Hello {uid}, enter your password: ")
			if user.get_password() == password:
				print(f"Welcome back, {user.get_name()}.")
			else:
				print("Incorrect password.")
	if not found:
		if edition == 2:
			signup(uid, 2)
		elif edition == 3:
			signup(uid, 3)


def signup(uid, edition):
	print(f"Hello {uid}, you need to sign up.")
	password = getpass("Password: ")
	email = input("Email: ")
	new_user = User(uid, password, email)
	if edition == 2:
		save_user(new_user, path_2e, 2)
	elif edition == 3:
		save_user(new_user, path_3e, 3)


def save_user(user, path, edition):
	if edition == 2:
		with open(path, "a", encoding="utf-8") as file:
			file.write(user.get_name() + delimiter)
			file.write(user.get_password() + delimiter)
			file.write(user.get_email() + delimiter)
			file.write(user.get_join_date() + "\n")
	elif edition == 3:
		line = user.get_name() + delimiter
		line += user.get_password() + delimiter
		line += user.get_email() + delimiter
		line += user.get_join_date() + "\n"
		# This overwrites the existing file :(
		# There is no append mode for path.write_text, lol?
		path.write_text(line)


users = load_users(path_2e, 2)
username = input("2nd edition - Hello, please enter your username: ")
if users:
	login(username, 2)
else:
	signup(username, 2)

users = load_users(path_3e, 3)
username = input("3rd edition - Hello, please enter your username: ")
if users:
	login(username, 3)
else:
	signup(username, 3)
