import error

# Numbers are stored as fractions in Orgy
# Numerator and denominator are named top and bottom, respectively, to keep up with S&M theme
class Fraction:
	def __init__(self, t, b):
		self.top = t
		self.bottom = b
		if t == 0 and b == 0:
			raise error.OrgyNumberError("Zero over zero is not allowed. You are dirty and deserve to be punished ;)")

	def to_string(self):
		return "{}/{}".format(self.top, self.bottom)
