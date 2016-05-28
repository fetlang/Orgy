import shlex
import error
import numparse
import ast


# After splitting into semi-meaningful words, the code is split into Token objects
class Token:
	def __init__(self, kin, lit, val, lin):
		# Kind of token
		self.kind = kin
		# The raw value
		self.literal = lit
		# What the value actually means
		self.value = val
		# Line number found on
		self.line = lin


class Tokenizer:
	# Take in raw source code
	def __init__(self, sourcecode):
		self.key_words = ["whip", "worship", "have", "her", "herself", "him", "himself", "them", "themself", "it",
						  "itself", "when", "if", "moreplease", "endif", "is", "over"]
		self.tokens = []
		self.words = []

		# Start tokenization
		self.raw_text = sourcecode
		self._split()
		self._remove_gags()
		self._tokenize()

		# Print out
		for i in self.tokens:
			print("({},{},{},{})".format(i.kind, i.literal, i.value, i.line))

	# Split self.raw_text into lines, and lines into semi-meaningful words
	# That is, words separated by spaces, and quotes
	def _split(self):
		# Split into lines
		lines = self.raw_text.split("\n")

		self.words = []
		for line in lines:
			# Prepare shlexer thing
			shlexer = shlex.shlex(line)
			shlexer.quotes = '"'
			shlexer.whitespace_split = True
			shlexer.commenters = ''  # Comments exist, but in a nontraditional way (GAG - UNGAG)

			# Add splat line to words
			self.words.append(list(shlexer))

	# Remove comments(gags) from self.words
	# Orgy programs always start gagged
	def _remove_gags(self):
		new_words = []
		gagged = True

		# Go through self.words and add only ungagged words to new_words
		for line in self.words:
			new_words.append([])
			for word in line:
				if gagged:
					if word.lower() == "ungag":
						gagged = False
				else:
					if word.lower() == "gag":
						gagged = True
					else:
						new_words[-1].append(word)

		# update self.words
		self.words = new_words

	def _tokenize(self):
		# Keep track of line numberings
		line_number = 0

		# Go through lines
		for line in self.words:
			line_number += 1

			# Go through line
			i = 0
			while i < len(line):
				word = line[i]

				# Convert keyword to token
				if word.lower() in self.key_words:
					self.tokens.append(Token("keyword", word, word.lower(), line_number))

				# Convert number to token
				elif numparse.within_number(word):
					number_start = i
					while i < len(line) - 1 and numparse.within_number(line[i + 1]):
						i += 1
					number = " ".join(line[number_start:i + 1])
					self.tokens.append(Token("fraction-literal", number, numparse.to_fraction(number), line_number))

				# Convert quote to token
				elif word[0] == '"':
					buffer = word

					# Join quotes
					while i < len(line) and line[i][-2] == '\\':
						if i >= len(line):
							raise error.OrgyTokenizerError("Multiline comments are not supported (line {})".format(line_number))
						buffer += line[i + 1]
						i += 1

					# Interpret quote
					quote = ast.literal_eval(buffer)

					self.tokens.append(Token("string-literal", buffer, quote, line_number))

				# Convert names to token
				else:
					name_start = i
					while i < len(line) - 1 and line[i + 1].lower() not in self.key_words and line[i + 1][0] != '"'\
						and not numparse.within_number(line[i + 1]):
						i += 1
					name = " ".join(line[name_start:i + 1])
					self.tokens.append(Token("name", name, name[0:name.index("'") if "'" in name else len(name)].lower(), line_number))
				i += 1


# Test
if __name__ == "__main__":
	Tokenizer("""UNGAG
	WHIP RICHARD STALLMAN NINE HUNDRED TIMES
	HAVE LINUS TORVALDS WORSHIP RICHARD STALLMAN'S FEET "what is going on \\" here?"
	""")
