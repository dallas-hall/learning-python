#!/usr/bin/python3
import logging, sys, os, time
import unittest
# To import this in PyCharm, right click the folder and mark as Sources Root
from survey import AnonymousSurvey

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

class TestAnonymousSurvey(unittest.TestCase):
	"""Test the AnonymousSurvey class"""

	# This is always run before every test_* is executed
	def setUp(self):
		# Create the AnonymousSurvey object
		question = "What language did you first learn to speak?"
		# Call the constructor
		self.my_survey = AnonymousSurvey(question)
		self.responses = ["English", "Korean", "Spanish"]

	def test_store_single_response(self):
		"""Test that a single response is stored correctly."""
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_three_responses(self):
		"""Test that three responses are stored correctly."""
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

	if __name__ == "__main__":
		unittest.main()
