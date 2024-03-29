import time
from datetime import datetime
from pytz import timezone


class User:
	"""A simple user object."""
	# The constructor, optional argument join_date that if not explicitly passed, is the current timestamp.
	def __init__(self, name, password, email,
	             join_date=datetime.now(timezone("Australia/Sydney")).strftime("%Y-%m-%d %H:%M:%S")):
		self.name = name
		self.password = password
		self.email = email
		self.join_date = join_date
		self.last_login_date = None
		self.successful_logins = 0
		self.failed_logins = 0

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
			self.add_successful_login()
		else:
			print(f"Incorrect email and/or password.")
			self.add_failed_login()

	def logout(self):
		print(f"Goodbye {self.name}.")

	def get_successful_logins(self):
		return self.successful_logins

	def add_successful_login(self):
		self.successful_logins += 1

	def get_failed_logins(self):
		return self.failed_logins

	def add_failed_login(self):
		self.failed_logins += 1
