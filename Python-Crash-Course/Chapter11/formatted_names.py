# Middle name and last name are optional.
def get_formatted_name(first, middle="", last=""):
	"""Generate a neatly formatted name."""
	if last:
		if middle:
			return f"{first} {middle} {last}".title()
		else:
			return f"{first} {last}".title()
	else:
		return f"{first}".title()
