import shlex
import error
import numparse
import ast
import keywords


# After splitting into semi-meaningful words, the code is split into Token objects
class Token:
	def __init__(self, kind, raw_value, value, line):
		# Kind of token
		self.kind = kind
		assert self.kind in ["keyword", "fraction-literal", "chain-literal", "identifier", "pronoun"]
		# The raw value
		self.raw_value = raw_value
		# What the raw_value actually means
		self.value = value
		# Line number found on
		self.line = line


class Tokenizer:
	# Take in raw source code
	def __init__(self, sourcecode):
		
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
			print("({},{},{},{})".format(i.kind, i.raw_value, i.value, i.line))

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
			#print(line)
			line_number += 1

			# Go through line
			i = 0
			while i < len(line):
				word = line[i]


				# Convert keyword to token
				if word.lower() in keywords.base_words:
					print("Probable:{}".format(word))
					j = 0
					# Look for full keyword
					while (i + 1 < len(line)) and " ".join([word,line[i+1]]).lower() in keywords.keywords:
						word = " ".join([word,line[i+1]])
						i += 1
						j += 1
					# False alarm - not actually a keyword
					if word.lower() not in keywords.keywords:
						print("Not lol:{}".format(word))
						i -= j
					# Add as token
					else:
						print("Confirm:{}".format(word))
						self.tokens.append(Token("keyword", word, word.lower(), line_number))
						i += 1
						continue

				# Convert number to token
				if numparse.within_number(word):
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

				# Check for non-posessive pronoun
				elif word.lower() in keywords.dictionary["objective pronouns"] or word.lower() in keywords.dictionary["reflexive pronouns"]:
					self.tokens.append(Token("pronoun", word, word.lower(), line_number))

				# Convert names or possesive pronouns to token
				else:
					name_start = i
					# Continue until start of literal is found
					while i < len(line) -1 and line[i + 1][0] != '"' and not numparse.within_number(line[i+1]):
						# Check if there is a beginning of a keyword
						if line[i + 1].lower() in keywords.base_words:
							# Oh shit, there is, What we gonna do?
							buf = ""
							k = i + 1
							it_is_a_keyword = False
							while k<len(line) and line[k].lower() in keywords.base_words:
								buf += line[k]+" "
								# Check if the buffer matches a keyword
								if buf[0:-1].lower() in keywords.keywords:
									# oh shiiiiiiiiit whadup it's a keyword
									it_is_a_keyword = True
									break
							if it_is_a_keyword:
								break
						i += 1
					# Final identifier name
					name = " ".join(line[name_start:i + 1])
					self.tokens.append(Token("identifier", name, name[0:name.index("'") if "'" in name else len(name)].lower(), line_number))
				i += 1


# Test
if __name__ == "__main__":
	Tokenizer("""UNGAG
	MORE PLEASE
	SPANK RICHARD STALLMAN NINE HUNDRED TIMES
	HAVE LINUS TORVALDS WORSHIP HIM now "what is going on \\" here?"
	""")
