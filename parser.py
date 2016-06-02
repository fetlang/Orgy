import tokenizer

# Syntax tree node
class Node (tokenizer.Token):
	def __init__(self, kind, literal = None, value = None, line = None, children = None):
		# Kind of token
		self.kind = kind
		assert self.kind in ["keyword", "fraction-literal", "chain-literal", "safeword", "variable", "special"]
		# The raw value
		self.literal = literal
		# What the value actually means
		self.value = value
		# Line number found on
		self.line = line
		# Child nodes
		self.children = [] if children == None else children
		
# Variable
class Variable:
	def __init__(self, kin, gender=None, iv=None):
		self.kind = kin; # Can be fraction or chain
		assert self.kind=="fraction" or self.kind=="chain"
		
		# Male, female, neutral, nonperson, None
		self.gender = gender
		assert self.gender in ["male", "female", "neutral", "nonperson", None]
		
		# Default value
		self.initial_value = iv
	
# Parser object converts a list of tokens into a syntax tree, to be
# passed to the transcompiler (to be passed to the C Compiler)
class Parser:
	def __init__(self, tokens):
		# syntax tree
		tree = Node()
		Node.kind = "root"
		_parse(tree);
		
	def _parse(self, root):
		if_block = 0
		while_block = 0  # Includes both while and until
		
		# Go through tokens
		for i in range(len(tokens)):
			token = tokens[i]
			
			if token.kind == "keyword":
			
				# Basic fraction operation
				if token.value in ["have","make","tie up", "beg", "whip","worship","feel up"]
					root.append(Node("operation",None, None, token.line))
					if token.value == "have":
						root[-1].insert(Node5r)
