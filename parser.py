import keywords
import operators
import random
import fraction
from variable import*
from error import *


# Syntax tree node
class Node:
	def __init__(self, kind, subkind=None, value=None, raw_value=None, line=None, children=None):
		self.kind = kind
		assert self.kind in ["root", "literal", "safeword", "variable", "operator", "comparison", "flow"]
		# Subcategory of token
		self.subkind = subkind
		assert self.subkind in [None, "fraction", "chain", "stream"]\
			   or self.subkind in keywords.operators

		# What was literally written by the programmer
		self.raw_value = raw_value
		# What the value actually means
		self.value = value
		# Line number found on
		self.line = line
		# Child nodes (as a list of moar nodes)
		self.children = [] if children is None else children


class Safeword:
	def __init__(self, name, scope):
		self.name = name
		self.scope = scope
		self.label = "_"+"".join(chr(random.randint(65, 65+25)) for _ in range(8))+"_orgy_label"


# Parser object converts a list of tokens into a syntax tree, to be
# passed to the transcompiler (to be passed to the C Compiler)
class Parser:
	def __init__(self, tokens):
		# syntax tree
		self.variables = builtin_variables
		self.tokens = tokens
		self.tree = Node("root")
		self._parse(self.tree)
		self.safewords = []

	def _token_to_node(self, token, line=None):
		if token.kind == "identifier":
			node = Node("variable", raw_value=token.raw_value, value=token.value, line=token.line)

	# Return a variable searched
	# Create variable if not found
	def _find_variable(self, name, kind, line):
		for i in self.variables:
			if i.name == name:
				# Assure kinds match, fraction to fraction, and chain/stream to chain
				if (kind == "fraction" and i.kind != "fraction") or (kind == "chain" and i.kind =="fraction"):
					raise OrgyParseError("{}: '{}' is a {}, not a {}".format(line, name, i.kind, kind))
				return name

		# Not found, so create
		self.variables.append(name, kind)
		return self.variables[-1]

	# Find the last accessed variable of that gender or None
	def _find_last_of_gender(self, var_list, gender):
		for i in var_list[::-1]:
			if i.gender in [None, gender]:
				i.gender = gender
				return i
		return None

	def _parse(self, root):
		if_block = 0
		while_block = 0  # Includes both while and until
		get_scope = lambda: if_block + while_block
		var_access_list = []

		# Go through tokens
		self.i = 0
		while self.i < len(self.tokens):
			token = self.tokens[self.i]
			
			if token.kind == "keyword":

				# Basic operation
				if token.value in ["have","make"] + keywords.dictionary["operators"]:
					rho = None
					lho = None
					operator = None
					if token.value in ["have", "make"]:
						# Interpret format like HAVE/MAKE <RHO/LHO> OPERATOR <LHO/[RHO]>
						if self.i+1 < len(self.tokens) and self.tokens[self.i+1].line == token.line:
							rho = self.tokens[self.i+1]
							if self.i+2 < len(self.tokens) and self.tokens[self.i+2].line == token.line:
								operator = self.tokens[self.i+2]
								if self.i+3 < len(self.tokens) and self.tokens[self.i+3].line == token.line:
									lho = self.tokens[self.i+3]
									self.i += 3
								elif token.value=="have":
									raise OrgyParseError("{}: expected operand after operator".format(token.line))
								else:
									self.i += 2
							else:
								raise OrgyParseError("{}: expected operator after operand".format(token.line))
						else:
							raise OrgyParseError("{}: expected operand after '{}'".format(token.line, token.raw_value))
						if token.value == "make":
							temp = lho
							lho = rho
							rho = temp
					else:
						# Interpret format like OPERATOR LHO [X TIMES]
						operator = token
						if self.i + 1 < len(self.tokens) and self.tokens[self.i + 1].line == token.line:
							lho = self.tokens[self.i+1]
							if self.i + 2 < len(self.tokens) and self.tokens[self.i + 2].line == token.line:
								if isinstance(self.tokens[self.i+2].value, fraction.Fraction):
									rho = self.tokens[self.i+2]
									if not (self.i + 3 < len(self.tokens) and self.tokens[self.i + 3].line == token.line and
										self.tokens[self.i+3].value == "times"):
										raise OrgyParseError("{} expected times after RHO".format(token.line))
									self.i += 3
								else:
									raise OrgyParseError("{}: only fraction literals are valid RHO's without make/have".format(token.line))
							else:
								self.i += 2

					# Make assertions
					if lho.kind not in ["pronoun", "identifier"]:
						raise OrgyParseError("{}: LHO's can only be pronouns or identifiers".format(token.line))
					if rho is not None:
						if rho.kind not in ["pronoun", "identifier", "fraction-literal", "chain-literal"]:
							raise OrgyParseError("{}: LHO's can only be pronouns, identifiers, or literals".format(token.line))
						if token.value == "make" and rho.kind == "fraction-literal":
							raise OrgyParseError("{}: RHO cannot be a fraction literal in this context".format(token.line))
					elif token.value == "have":
						raise OrgyParseError("{}: RHO needed for 'HAVE'".format(token.line))
					if token.value == "have" and rho.kind in ["fraction-literal", "chain-literal"]:
						raise OrgyParseError("{}: RHO cannot be a literal in this context".format(token.line))
					if operator.value not in keywords.dictionary["operators"]:
						raise OrgyParseError("{}: '{}' is not an operator".format(token.line, operator.raw_value))

					# Handle reflexive pronouns:
					if lho.kind == "pronoun" and lho.value in keywords.dictionary["reflexive"]:
						if token.value == "have":
							lho = rho
						else:
							raise OrgyParseError("{}: didn't expect reflexive pronoun here".format(token.line))
					elif rho.kind == "pronoun" and rho.value in keywords.dictionary["reflexive"]:
						if token.value == "make":
							rho = lho
						else:
							raise OrgyParseError("{}: didn't expect reflexive pronoun here".format(token.line))


					# Convert operator into Node
					for op in operators.operators:
						if operator.value == op.name:
							operator = Node("operator", None, op, operator.raw_value)
							break

					# Convert operands in to Nodes
					operands = []value =
					for operand in [lho, rho]:
						if operand is None:

						# Handle objective pronouns
						elif operand.kind == "pronoun":
							gender = None
							if operand.value == "them":
								gender = "neutral"
							elif operand.value == "him":
								gender= "male"
							elif operand.value == "her":
								gender ="female"
							elif operand.value = "it":
								gender = "nonperson"
							else:
								raise OrgyParseError("{}: no gender for {}".format(token.line, operand.value))
							var = self._find_last_of_gender(var_access_list, gender)
							if var is None:
								raise OrgyParseError("{}: no gender-appropriate variable found".format(token.line))
							if var.subkind is None:
								raise OrgyParseError("{}: subkind is None".format(token.line))

							# Make variable node from pronoun
							operands.append(Node("variable", var.subkind, var, operand.raw_value, operand.line))
						elif operand.kind == "identifier":
							operands.append(Node("variable", operand.subkind, ))

					# We know the lho, operator, and rho, so we can parse generically now






			self.i += 1