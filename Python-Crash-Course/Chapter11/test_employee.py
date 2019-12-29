#!/usr/bin/python3
import logging, sys, os, time
import unittest
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

class EmployeeTestCase(unittest.TestCase):
	"""
	Test cases for employee class.
	"""

	# This is always run before every test_* is executed
	def setUp(self):
		# Create variables for testing
		names = ["John Doe", "Jane Doe"]
		self.employees = []
		for name in names:
			new_employee = Employee(name, "IT")
			self.employees.append(new_employee)

	def test_employees_added(self):
		for employee in self.employees:
			self.assertIn(employee, self.employees)

	def test_give_default_raise(self):
		self.employees[0].increase_salary()
		self.assertEqual(self.employees[0].salary, 25000)

	def test_give_specific_raise(self):
		self.employees[0].increase_salary(15000)
		self.assertEqual(self.employees[0].salary, 35000)

	if __name__ == "__main__":
		unittest.main()
