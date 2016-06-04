# This module parses English short scale numbers into fractions

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


# Number words groups, separated by grammar
_singles = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
_teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
_adults = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
_mature = ["thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]
_special = ["zero", "negative", "positive", "over"]


# Convert a single word to an integer (not including zero, since it is a special grammatical case)
def _word_to_int(word):
	if word in _singles:
		return _singles.index(word) + 1
	if word in _teens:
		return _teens.index(word) + 10
	if word in _adults:
		return (_adults.index(word) + 2) * 10
	if word in _mature:
		return 10 ** (3 * (_mature.index(word) + 1))
	if word == "hundred":
		return 100
	if "-" in word[0:-1] and word[0:word.index("-")] in _adults and word[word.index("-") + 1::] in _singles:
		return _word_to_int(word[0:word.index("-")]) + _word_to_int(word[word.index("-") + 1::])
	else:
		return None


def _word_to_int_safe(word):
	number = _word_to_int(word)
	if number is None:
		raise error.OrgyNumberError("{} is not a valid number".format(word))
	return number


# Convert a "triple" (anything split by thousand, million, etc) to an integer
def _triple_to_int(triple_string):
	not_valid = "'{}' is not a valid triple".format(triple_string)
	# Convert string to list
	triple = triple_string.split()

	# Remove "and" at beginning
	if triple[0].lower() == "and":
		triple = triple[1::]

	# Check for basic errors
	if len(triple) == 0:
		raise error.OrgyNumberError("Triple is empty")
	elif len(triple) >= 3 and triple[2].lower() != "and":
		raise error.OrgyNumberError("Expected 'and', found '{}'".format(triple[2]))
	elif len(triple) == 3:
		raise error.OrgyNumberError(not_valid)
	elif len(triple) > 5:
		raise error.OrgyNumberError("Triple '{}' is too long (max 5 words)".format(triple_string))

	# Start parsing

	# Triple is of the form (one), (ten), (twenty) or (twenty-one)
	elif len(triple) == 1:
		number = _word_to_int_safe(triple[0].lower())
		if 0 < number < 100:
			return number
		else:
			raise error.OrgyNumberError("'{}' by itself is not a valid triple".format(triple[0]))

	# Triple is of the form (one hundred) or (twenty two)
	elif len(triple) == 2:
		if triple[0].lower() in _singles and triple[1].lower() == "hundred":
			return _word_to_int_safe(triple[0].lower()) * 100
		elif triple[0].lower() in _adults and triple[1].lower() in _singles:
			return _word_to_int_safe(triple[0].lower()) + _word_to_int_safe(triple[1].lower())
		else:
			raise error.OrgyNumberError(not_valid)

	# Triple is of the form (one hundred and X) or (one hundred and X Y)
	else:
		fourth = _word_to_int_safe(triple[3].lower())
		fifth = 0
		if len(triple) == 5:
			fifth = _word_to_int_safe(triple[4].lower())
		if triple[0].lower() in _singles and triple[1].lower() == "hundred":
			number = _word_to_int_safe(triple[0].lower()) * 100
			if len(triple) == 4 and 0 < fourth < 100:
				return number + fourth
			elif len(triple) == 5 and triple[3].lower() in _adults and triple[4].lower() in _singles:
				return number + fourth + fifth
			else:
				raise error.OrgyNumberError(not_valid)
		else:
				raise error.OrgyNumberError(not_valid)


# Convert a number like ["five" "thousand" "two hundred and eighty-nine"] to 5289
def _number_to_int(number):
	temp = 0
	result = 0

	# Check for zero special case
	if len(number) == 1 and number[0].lower() == "zero":
		return 0

	# Sum to get result
	for token in number:
		if token.lower() in _mature:
			result += temp * _word_to_int_safe(token.lower())
			temp = 0
		else:
			temp = _triple_to_int(token)

	# Check last part
	if number[-1].lower() not in _mature:
		result += temp
	return result


# Convert words like "negative two over five thousand eight hundred and twelve" to Fraction(-2, 5812)
def to_fraction(words):
	# Split into tokens (specials and triples)
	tokens = []
	buffer = ""
	for word in words.split():
		if word.lower() in _special + _mature:
			if buffer != "":
				tokens.append(buffer)
				buffer = ""
			tokens.append(word)
		else:
			if buffer != "":
				buffer += " "
			buffer += word
	if buffer != "":
		tokens.append(buffer)

	# Set pointer to zero
	pointer = 0

	# Check for negativity
	negative = False
	if tokens[0].lower() == "negative":
		negative = True
		pointer += 1

	# Parse
	if "over" in (token.lower() for token in tokens):
		# "over" means there is a numerator and a dominator (power bottom)
		top = _number_to_int(tokens[pointer:[token.lower() for token in tokens].index("over")])
		bottom = _number_to_int(tokens[[token.lower() for token in tokens].index("over") + 1::])
	else:
		# No dominator, just numerator
		top = _number_to_int(tokens[pointer::])
		bottom = 1

	if negative:
		top = -top

	# Return as fraction
	return Fraction(top, bottom)


# Check if words are numbers for tokenization
def within_number(word):
	if word.lower() in _special or _word_to_int(word.lower()) is not None:
		return True
	else:
		return False


# Test
if __name__ == "__main__":
		line = "negative three billion forty-two million five thousand and six"
		print(to_fraction(line.lower()).to_string())
		print(to_fraction(line.upper()).to_string())
		print(to_fraction("one").to_string())
		print(to_fraction("zero").to_string())
