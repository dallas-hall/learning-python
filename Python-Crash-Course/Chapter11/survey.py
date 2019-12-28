class AnonymousSurvey:
	""" Collect anonymous answers to a survey question."""

	# The constructor
	def __init__(self, question):
		"""Store the question and answers."""
		self.question = question
		self.responses = []

	def show_question(self):
		"""Show the survey question"""
		print(f"{self.question}")

	def store_response(self, new_response):
		"""Store a single response."""
		self.responses.append(new_response)

	def show_results(self):
		"""Show all the responses that have been given."""
		print("Survey results:")
		for response in self.responses:
			print(f"- {response}")
