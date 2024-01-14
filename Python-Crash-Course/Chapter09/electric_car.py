# To import this in PyCharm, right click the folder and mark as Sources Root
# If you just use import car, you need ot use car dot notation. Good for avoiding naming conflicts.
from car import Car


# Car was moved into car.py to showcase modules. It could be defined here too.
# Use inheritance to create a sub class
class ElectricCar(Car):
	"""A simple EV object that is a subclass of Car."""
	# Call the constructor of the super class
	def __init__(self, make, model, year):
		# Inherited superclass attributes via superclass constructor
		super().__init__(make, model, year)
		# subclass attributes
		# Using another class instance to represent the battery, constructor call.
		self.battery = Battery(100)

	# Similar to a Java override
	def get_details(self):
		return super().get_details() + f", {self.battery.size} kWh battery at {self.battery.charge} kWh charge, and battery health is {self.battery.health}."


# This could go into its own file.
class Battery:
	"""A simple battery class."""
	# size is an optional parameter, use the default of 75 if it isn't supplied
	def __init__(self, size=75):
		self.size = size
		# Fully charged
		self.charge = size
		self.health = 'Good'

	def charge_battery(self):
		if self.charge < 100:
			self.charge += 1
		else:
			print("Cannot charge battery above 100.")

	def discharge_battery(self):
		self.charge -= 1

	def update_battery_charge(self, kilowatts):
		if self.charge - kilowatts >= 0:
			self.charge -= kilowatts
		else:
			print("Cannot discharge battery below 0.")

	def get_details(self):
		return f"Battery size is {self.size} kWh, the current charge is {self.charge}%, and the health is {self.health}."
