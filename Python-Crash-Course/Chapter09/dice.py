from random import randint

class Dice:
	def __init__(self, sides):
		self.sides = sides

	def get_sides(self):
		return self.sides

	def roll_dice(self):
		# Generate a random number between 2 numbers, inclusive.
		return randint(1, self.sides)

