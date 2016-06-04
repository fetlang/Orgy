class OrgyError(Exception):
	def __init__(self, val, line=None):
		self.value = val
		self.line = line


class OrgyNumberError(OrgyError):
	pass


class OrgyTokenizerError(OrgyError):
	pass
