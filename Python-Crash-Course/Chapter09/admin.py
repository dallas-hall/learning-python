from user import User
from privileges import Privileges


# Need to send the superclass as a parameter for the subclass
class Admin(User):
	"""A simple administrator class that is a subclass of User."""
	def __init__(self, name, password, email, os):
		super().__init__(name, password, email)
		self.os_privileges = Privileges(os)
