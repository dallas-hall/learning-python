#!/usr/bin/python3
import logging, sys, os, time
# To import this in PyCharm, right click the folder and mark as Sources Root
# If you just use import car, you need ot use car dot notation. Good for avoiding naming conflicts.
from car import Car

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

# Car was moved into car.py to showcase modules. It could be defined here too.


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


# This could go into its own file.
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