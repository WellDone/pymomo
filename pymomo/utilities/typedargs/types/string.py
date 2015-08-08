def convert(arg):
	if arg is None:
		return None

	return str(arg)

def validate_list(arg, choices):
	"""
	Make sure the argument is in the list of choices passed to the function
	"""
	
	choice_set = set(choices)

	if arg not in choices:
		raise ValueError('Value not in list: %s' % str(choices))

def validate_not_empty(arg):
	"""
	Make sure the string is not empty
	"""

	if len(arg) == 0:
		raise ValueError("String cannot be empty")

def default_formatter(arg, **kwargs):
	return arg

def format_repr(arg, **kwargs):
	return repr(arg)