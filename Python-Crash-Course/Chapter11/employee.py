import time
from datetime import datetime
from pytz import timezone


class Employee:
	"""
	A class that models an organisational employee.
	"""
	# Constructor with optional parameters that have default values
	def __init__(self, name, department, salary=50000,
	             hire_date=datetime.now(timezone("Australia/Sydney")).strftime("%Y-%m-%d %H:%M:%S")):
		self.name = name
		self.department = department
		self.salary = salary
		self.hire_date = hire_date

	def print_details(self):
		print(f"{self.name} started working at {self.department} on {self.hire_date} and earns {self.salary}")

	# Optional 5000 dollar increase
	def increase_salary(self, increase=5000):
		self.salary += increase

	def set_department(self, department):
		self.department = department
