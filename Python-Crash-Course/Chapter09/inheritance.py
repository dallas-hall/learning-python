#!/usr/bin/python3
import logging, sys, os, time

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

# Superclass must be in the same file and before the sub class(es)
class Car:
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
		self.odometer += kilometers


# Use inheritance to create a sub class
class ElectricCar(Car):
	# Call the constructor of the super class
	def __init__(self, make, model, year):
		# Inherited superclass attributes via superclass constructor
		super().__init__(make, model, year)
		# subclass attributes
		# Using another class instance to represent the battery, constructor call.
		self.battery = Battery(100)

	# Similar to a Java override
	def get_details(self):
		return super().get_details() + f" {self.battery.size} kWh battery at {self.battery.charge} kWh charge."


class Battery:
	# size is an optional parameter, use the default of 75 if it isn't supplied
	def __init__(self, size=75):
		self.size = size
		# Fully charged
		self.charge = size

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


car1 = Car("Ford", "Falcon", "1999")
print(car1.get_details())
car2 = ElectricCar("Tesla", "Roadster", "2018")
print(car2.get_details())