class Privileges:
	# Constructor, optional os parameter that defaults to linux
	def __init__(self, os="linux"):
		if os.lower() == "linux":
			self.linux_admin = True
			self.windows_admin = False
		elif os.lower() == "windows":
			self.linux_admin = False
			self.windows_admin = True

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
