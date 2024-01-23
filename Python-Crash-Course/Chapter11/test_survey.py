import pytest
# To import this in PyCharm, right click the folder and mark as Sources Root
from survey import AnonymousSurvey


# Use a pytest decorator to create a test fixture that can be used by all testing functions.
@pytest.fixture
def language_survey():
	"""A survey that will be used by all test functions."""
	question = "What language did you first learn to speak?"
	language_survey = AnonymousSurvey(question)
	return language_survey


# When a parameter matches the name of a @pytest.fixture decorator, the decorator will automatically run.
def test_store_single_response(language_survey):
	"""Test that a single response is stored correctly."""
	language_survey.store_response("English")
	assert "English" in language_survey.responses


def test_store_three_responses(language_survey):
	"""Test that three responses are stored correctly."""
	responses = ["English", "Korean", "Spanish"]
	for response in responses:
		language_survey.store_response(response)
	assert len(language_survey.responses) == 3
	for response in responses:
		assert response in language_survey.responses
