# Middle name and last name are optional.
def get_formatted_name(first, last="", middle=""):
	"""Generate a neatly formatted name."""
	if last is not "":
		if middle is not "":
			return f"{first} {middle} {last}".title()
		else:
			return f"{first} {last}".title()
	else:
		return f"{first}".title()
