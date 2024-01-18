#!/usr/bin/env python3
import logging, sys, os, time
# To import this in PyCharm, right click the folder and mark as Sources Root
import car
# Import multiple classes from the same file. Also using an alias.
from electric_car import ElectricCar as EC, Battery

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = False
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.100)

print('Creating the first car.')
# Need to use dot notation here since we did `import car`
car1 = car.Car("Ford", "Falcon", "1999")
print(car1.get_details())
print(car1.get_details())
car1.increment_odometer(10_000)
car1.increment_odometer_by_100()
print(car1.get_details())
car1.update_odometer(0)
car1.increment_odometer(-10_000)

print('\nCreating the second car.')
# Don't need to use dot notation here since we did `from electric_car import ElectricCar as EC, Battery`
# Using the EC alias we defined above.
car2 = EC("Tesla", "Roadster", "2018")
print(car2.get_details())
print("Driving car.")

car2.battery.update_battery_charge(50)
print(car2.get_details())
print("Charging car by 30%.")
for i in range(1, 31):
	car2.battery.charge_battery()
print(car2.battery.get_details())

print('\nCreating a generic battery.')
my_battery = Battery(10)
print(my_battery.get_details())
