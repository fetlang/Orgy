import hashlib
import error


# Variable class
class Variable:
	def __init__(self, name, kind, value=None, gender=None, permissions=None):
		self.name = name.lower()
		self.kind = kind
		self._value = value  # Value is None if it is a REGULAR VARIABLE
		self.gender = gender
		self._permissions = "rw" if permissions is None else permissions
		self.fileno = value if kind == "stream" else None

		# Debug
		assert self.kind in ["chain", "fraction", "stream"]
		assert self._permissions in ["r","w","rw","wr"]
		assert self.gender in [None, "male", "female", "neutral", "nonperson", "n/a"]

	# Return C code
	# For a normal variable, return the MD5 hash + a tail and a head
	def get_code(self, access):
		if access[0] not in self._permissions:
			raise error.OrgyParseError("Inappropriate access: '{}' to var with '{}' privs".format(access, self._permissions))
		if self.kind == "stream":
				return "WRITING_BUFFER" if access[0] == "w" else "READING_BUFFER"
		if self._value is None:
			self._value = "_" + hashlib.md5(self.name.encode("UTF-8")).hexdigest()+"_orgy_variable"
		return self._value


# List of all variables
builtin_variables = [Variable("NAUGHTY", "fraction", value="construct_fraction(0,1)", gender="n/a", permissions="r"),
			 Variable("LEONHARD EULER", "fraction", "construct_fraction(271801,99990)","male","r"),
			 Variable("CHRONOS", "fraction", "time_fraction()","male","r"),
			 Variable("ERIS", "fraction","random_fraction()","female","r"),
			 Variable("BRUCE SCHNEIER", "fraction", "cryptorandom_fraction()", "male", "r"),
			 Variable("MISTRESS", "stream", 0, "female","rw"),
			 Variable("SLAVE", "stream", 1, "male", "rw")]
