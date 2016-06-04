import shlex
import error
import numparse
import ast


# After splitting into semi-meaningful words, the code is split into Token objects
class Token:
	def __init__(self, kin, lit, val, lin):
		# Kind of token
		self.kind = kin
		assert self.kind in ["keyword", "fraction-literal", "chain-literal", "name"]
		# The raw value
		self.literal = lit
		# What the value actually means
		self.value = val
		# Line number found on
		self.line = lin


class Tokenizer:
	# Take in raw source code
	def __init__(self, sourcecode):
		# Proper key word
		self.key_words = ["whip", "worship", "have", "her", "herself", "him", "himself", "them", "themself", "it",
						"itself", "when", "if", "is"]
		# Proper key words involving more than one word
		self.compound_words = ["is over", "is under", "more please", "tie up", "end if", "feel up", "is not"]
		# All reserved words
		self.reserved_words = list(set(self.key_words + " ".join(self.compound_words).split()))
		print(self.reserved_words)
		
		# List of tokens (permanent) and words(temporary)
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
			shlexer.commenters = ''  # Comments exist, but as (GAG...UNGAG)

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

				# Convert reserved word to token
				if word.lower() in self.reserved_words:
					if i + 1 < len(line) and " ".join(line[i:i + 2]).lower() in self.compound_words:
						word = " ".join(line[i:i + 2])
						i += 1
					elif word.lower() not in self.key_words:
						raise error.OrgyTokenizerError("expected another word after {}".format(word), line_number)
					self.tokens.append(Token("keyword", word, word.lower(), line_number))

				# Convert number to token
				elif numparse.within_number(word):
					number_start = i
					# Check if next (and the next) word is part of the number
					while i < len(line) - 1 and numparse.within_number(line[i + 1]):
						i += 1
					# Join the whole number
					number = " ".join(line[number_start:i + 1])
					# Interpret as fraction at append as token
					self.tokens.append(Token("fraction-literal", number, numparse.to_fraction(number), line_number))

				# Convert quote to token
				elif word[0] == '"':
					# Buffer holds the *entire* quote, to be evaluated
					buffer = word

					# Join quotes that were unfortunate to be wrongly separated by an escapes quote
					while i < len(line) and line[i][-2] == '\\':
						if i >= len(line):
							raise error.OrgyTokenizerError("Multiline quotes are not supported (line {})".format(line_number))
						buffer += line[i + 1]
						i += 1

					# Interpret quote
					quote = ast.literal_eval(buffer)

					# Define token as chain literal
					self.tokens.append(Token("chain-literal", buffer, quote, line_number))

				# Convert names to token
				else:
					name_start = i
					while i < len(line) - 1 and line[i + 1].lower() not in self.reserved_words and line[i + 1][0] != '"'\
						and not numparse.within_number(line[i + 1]):
						i += 1
					name = " ".join(line[name_start:i + 1])
					self.tokens.append(Token("name", name, name[0:name.index("'") if "'" in name else len(name)].lower(), line_number))
				i += 1


# Test
if __name__ == "__main__":
	Tokenizer("""UNGAG
	MORE PLEASE
	WHIP RICHARD STALLMAN NINE HUNDRED TIMES
	HAVE LINUS TORVALDS WORSHIP RICHARD STALLMAN'S FEET "what is going on \\" here?"
	""")
