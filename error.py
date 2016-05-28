class OrgyError(Exception):
	def __init__(self, val):
		self.value = val


class OrgyNumberError(OrgyError):
	pass


class OrgyTokenizerError(OrgyError):
	pass
