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


	def test_store_single_response(self):
		"""Test that a single response is stored correctly."""
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		my_survey.store_response("English")
		self.assertIn("English", my_survey.responses)

	def test_store_three_responses(self):
		"""Test that a single response is stored correctly."""
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		responses = ["English", "Korean", "Spanish"]
		for response in responses:
			my_survey.store_response(response)
		for response in responses:
			self.assertIn(response, my_survey.responses)

	if __name__ == "__main__":
		unittest.main()
