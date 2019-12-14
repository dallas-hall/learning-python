#!/usr/bin/python3
import logging, sys, os, time
import unittest
# In PyCharm, right click > Mark Directory As ? Sources root
from formatted_names import get_formatted_name

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

class NamesTestCase(unittest.TestCase):
	"""Testing the formatted_names.py file."""

	# Function name must start with test_ so its run automatically.
	def test_first_name(self):
		"""Does a single name work?"""
		result = get_formatted_name("Ronaldo")
		self.assertEqual(result, "Ronaldo")

	def test_first_last_name(self):
		"""Does a first and last name work?"""
		result = get_formatted_name("janis", "", "joplin")
		self.assertEqual(result, "Janis Joplin")

	def test_first_middle_last_name(self):
		"""Does a full name of first, middle, and last name work?"""
		result = get_formatted_name("lee", "harvey", "OSWALD")
		self.assertEqual(result, "Lee Harvey Oswald")


if __name__ == "__main__":
	unittest.main()
