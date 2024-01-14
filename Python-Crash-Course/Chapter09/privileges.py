class Privileges:
	"""A simple privileges class that is used by Admin."""
	# Constructor, optional os parameter that defaults to linux.
	def __init__(self, os="linux"):
		if os.lower() == "linux":
			self.linux_admin = True
			self.windows_admin = False
			self.mac_admin = False
		elif os.lower() == "windows":
			self.linux_admin = False
			self.windows_admin = True
			self.mac_admin = False
		elif os.lower() == "mac":
			self.linux_admin = False
			self.windows_admin = False
			self.mac_admin = True

	def is_windows_admin(self):
		if self.windows_admin:
			return True
		else:
			return False

	def is_linux_admin(self):
		if self.linux_admin:
			return True
		else:
			return False

	def is_mac_admin(self):
		if self.mac_admin:
			return True
		else:
			return False
