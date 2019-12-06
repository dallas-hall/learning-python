import time
from datetime import datetime
from pytz import timezone


class User:
	# The constructor
	def __init__(self, name, password, email):
		self.name = name
		self.password = password
		self.email = email
		self.join_date = datetime.now(timezone("Australia/Sydney")).strftime("%Y-%m-%d %H:%M:%S")
		self.last_login_date = self.join_date

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

	def login(self, email, password):
		# Sleep to simulate hashing
		time.sleep(1)
		if self.email == email and self.password == password:
			print(f"Welcome {self.name}.")
			self.last_login_date = datetime.now(timezone("Australia/Sydney")).strftime("%Y-%m-%d %H:%M:%S")
		else:
			print(f"Incorrect email and/or password.")
