#!/usr/bin/python3
import logging, sys, os, time
# To import this in PyCharm, right click the folder and mark as Sources Root
from employee import Employee

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

names = ["John Doe", "Jane Doe"]
employess = []

for name in names:
	new_employee = Employee(name, "IT")
	employess.append(new_employee)

for employee in employess:
	employee.print_details()



