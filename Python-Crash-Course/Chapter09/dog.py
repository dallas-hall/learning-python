#!/usr/bin/env python
import logging, sys, os, time

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.100)


# Define a class, capitalised names refer to classes in Python
class Dog:
	"""
	A simple model of a dog.
	"""

	# The class constructor
	# self is required and must come before all other parameters.
	# self is the reference to the object instance and is passed implicitly to all class methods.
	def __init__(self, name, age, sex):
		"""
		Initialise the object state.
		:param name: Dog's name.
		:param age: Dog's age.
		:param age: Dog's sex.
		"""
		# These variables are accessible anywhere in the class.
		self.name = name
		self.age = age
		self.sex = sex

	# self needs to be passed in even if we aren't passing in any other attributes.
	# It is implicitly passed in.
	def sit(self):
		if self.sex.lower() == 'female':
			print(f"{self.name} is sitting like a good girl.")
		elif self.sex.lower() == 'male':
			print(f"{self.name} is sitting like a good boy.")

	def roll_over(self):
		print(f"Awww {self.name} rolled over for a belly rub.")


# self is passed automatically to the constructor and instance methods.
my_old_dog = Dog('Pierre', 10, 'male')
print(f"My old dog's name was {my_old_dog.name}.")
print(f"He was {my_old_dog.age} when he died.")
my_old_dog.sit()
my_old_dog.roll_over()

my_wifes_old_dog = Dog("Shoo Shoo", 7, 'female')
print(f"My wife's old dog's name was {my_wifes_old_dog.name}.")
print(f"She was {my_wifes_old_dog.age} when she died.")
my_wifes_old_dog.sit()
my_wifes_old_dog.roll_over()
