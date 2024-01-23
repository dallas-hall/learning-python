from formatted_names import get_formatted_name


# pytest will search for files named test_ and run them automatically.
# Function name must start with test_ so its run automatically.
def test_first_name():
	"""Does a single name work?"""
	result = get_formatted_name("Ronaldo")
	assert result == "Ronaldo"


def test_first_last_name():
	"""Does a first and last name work?"""
	result = get_formatted_name("janis", "", "joplin")
	assert result == "Janis Joplin"


def test_first_middle_last_name():
	"""Does a full name of first, middle, and last name work?"""
	result = get_formatted_name("lee", "harvey", "OSWALD")
	assert result == "Lee Harvey Oswald"
