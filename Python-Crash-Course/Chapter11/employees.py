#!/usr/bin/env python3
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
time.sleep(.100)

new_hires = {
	'John Doe': {
		'department': 'HR'
	},
	'Jane Doe': {
		'department': 'IT',
		'salary': 75_000
	},

}
employees = []

for key, value in new_hires.items():
	if value.get('salary'):
		employee = Employee(key, value['department'], value['salary'])
	else:
		employee = Employee(key, value['department'])
	employees.append(employee)

for employee in employees:
	employee.print_details()

for employee in employees:
	employee.increase_salary()

for employee in employees:
	employee.print_details()
