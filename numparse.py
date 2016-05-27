# Numbers are stored as fractions in Orgy
# Numerator and denominator are named top and bottom, respectively to keep up with S&M theme
class Fraction:
	def __init__(self, t, b):
		self.top = t
		self.bottom = b


# Number words groups, separated by grammar
_singles = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
_teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
_adults = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
_older = ["thousand", "million", "billion", "trillion"]
