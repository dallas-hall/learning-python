#!/usr/bin/python3
import logging, sys, os, time
from datetime import datetime
from pytz import timezone

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

class User:
	# The constructor
	def __init__(self, name, password, email):
		self.name = name
		self.password = password
		self.email = email
		self.join_date = datetime.now(timezone("Australia/Sydney")).strftime("%Y-%m-%d %H:%M:%S")

	def get_name(self):
		return self.name

	def get_password(self):
		return self.password

	def set_password(self, password):
		self.password = password

	def get_email(self):
		return self.email

	def set_email(self, email):
		self.email = email

	def get_join_date(self):
		return self.join_date


users = [
	User("Alice", "abc123", "alice@gmail.com"),
	User("Bob", "password", "bob@gmail.com")
]

for user in users:
	print(f"The current user's name is {user.name}.")
	print(f"The current user's password is {user.password}. Yeah, we store passwords in plaintext, YOLO.")
	print(f"The current user's email is {user.email}.")
	print(f"The current user's join date is {user.join_date}.")



