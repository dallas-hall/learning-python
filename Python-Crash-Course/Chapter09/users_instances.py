#!/usr/bin/env python
import logging, sys, os, time
# To import this in PyCharm, right click the folder and mark as Sources Root
from user import User
# By just importing admin we can use dot notation to avoid naming conflicts.
import admin

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.100)

users = [
	admin.Admin("Alice", "abc123", "alice@gmail.com", "linux"),
	User("Bob", "password", "bob@gmail.com"),
	admin.Admin("Charles", "password1", "charlie@hotmail.com", "mac")
]

for user in users:
	print(f"The current user's name is {user.name}.")
	print(f"The current user's password is {user.password}. Yeah, we store passwords in plaintext, YOLO.")
	print(f"The current user's email is {user.email}.")
	print(f"The current user's join date is {user.join_date}.")
	if user.name == "Alice":
		# Increment Alice's successful login counter
		user.login("alice@gmail.com", "abc123")
		user.logout()
		user.login("alice@gmail.com", "abc123")
	elif user.name == "Bob":
		user.login("bob@gmail.com", "passw0rd")
	if user.last_login_date is not None:
		print(f"The current user's last login date is {user.last_login_date}.")
	else:
		print(f"The current user has never logged in.")
	if type(user) is admin.Admin:
		if user.os_privileges.is_linux_admin():
			print("This user can administrate Linux")
		if user.os_privileges.is_windows_admin():
			print("This user can administrate Windows")
		if user.os_privileges.is_mac_admin():
			print("This user can administrate Mac OS.")
	print(f"The current amount of successful logins for {user.get_name()} is {user.get_successful_logins()}")
	print(f"The current amount of failed logins for {user.get_name()} is {user.get_failed_logins()}")
