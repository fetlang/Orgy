import keywords
import random
from variable import*
from error import *


# Syntax tree node
class Node:
	def __init__(self, kind, subkind=None, value=None, raw_value=None, line=None, children=None):
		self.kind = kind
		assert self.kind in ["root", "literal", "safeword","variable", "operator", "comparison", "flow"]
		# Subcategory of token
		self.subkind = subkind
		assert self.subkind in [None, "fraction", "chain", "objective", "reflexive"]\
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
		tree = Node("root")
		self._parse(tree)
		self.safewords = []

	def _token_to_node(self, token, line=None):
		if token.kind == "identifier":
			node = Node("variable", raw_value=token.raw_value, value=token.value, line=token.line)


	def _parse(self, root):
		if_block = 0
		while_block = 0  # Includes both while and until
		get_scope = lambda: if_block + while_block

		# Go through tokens
		for i in range(len(self.tokens)):
			token = self.tokens[i]
			
			if token.kind == "keyword":

				# Basic operation
				if token.value in ["have","make"] + keywords.operators:
					root.append(Node("operation", line=token.line))
					if token.value == "have":
						root[-1].insert(self._token_to_node(self.tokens[i+1]))
