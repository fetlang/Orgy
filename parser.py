import lexer
import keywords


# Syntax tree node
class Node:
	def __init__(self, category, subcategory=None, literal=None, value=None, line=None, children=None):
		# Category of token
		self.category = category
		assert self.category in ["root", "literal", "safeword", "variable", "stream",
								 "operation", "pronoun"]

		# Subcategory of token
		self.subcategory = subcategory
		assert self.subcategory in [None, "fraction", "chain", "input", "output"] or self.subcategory in keywords.operators

		# The raw value
		self.literal = literal
		# What the value actually means
		self.value = value
		# Line number found on
		self.line = line
		# Child nodes
		self.children = [] if children is None else children

	
# Parser object converts a list of tokens into a syntax tree, to be
# passed to the transcompiler (to be passed to the C Compiler)
class Parser:
	def __init__(self, tokens):
		# syntax tree
		self.tokens = tokens
		tree = Node("root")
		self._parse(tree)
		self.safewords = []

	def _token_to_node(self, token, line=None):
		if token.kind == "name":
			if token.value in self.safewords:
				node = Node("safeword", literal=token.literal, value=token.value, line=token.line)
			else:
				node = Node("variable", literal=token.literal, value=token.value, line=token.line)

		
	def _parse(self, root):
		if_block = 0
		while_block = 0  # Includes both while and until
		
		# Go through tokens
		for i in range(len(self.tokens)):
			token = self.tokens[i]
			
			if token.kind == "keyword":
			
				# Basic operation
				if token.value in ["have","make"] + keywords.operators:
					root.append(Node("operation", line=token.line))
					if token.value == "have":
						root[-1].insert(self._token_to_node(self.tokens[i+1]))
