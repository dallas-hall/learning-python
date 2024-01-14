# Superclass must be in the same file and before the sub class(es)
class Car:
	"""A Simple car object."""
	# Constructor
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0

	def get_details(self):
		return f"{self.year} {self.make} {self.model} {self.odometer} km"

	def read_odometer(self):
		return f"{self.odometer}"

	def update_odometer(self, kilometers):
		if kilometers >= self.odometer:
			self.odometer = kilometers
		else:
			print("Cannot roll back the odometer.")

	def increment_odometer(self, kilometers):
		if kilometers > 0:
			self.odometer += kilometers
		else:
			print("Kilometers cannot be 0 or negative.")

	def increment_odometer_by_100(self):
		self.odometer += 100
