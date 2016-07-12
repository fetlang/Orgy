# The purpose of this module is to neatly define Orgy operators
from fraction import Fraction


class Operator:
	def __init__(self, name, meaning, code, grammar=None, alt=None, default=None):
		self.name = name
		self.alt = alt
		# meaning: add, subtract, concat, concat_with_newline, etc
		self.meaning = meaning
		# Grammars can be 'have','make', 'plain'
		self.grammar = grammar
		# Default RH value
		self.default = default
		# Data types of the RHO and LHO
		self.code = code

# Normal Operators
operators = [
	Operator("spank", "subtract",
			 grammar=["have", "plain"],
			 default=Fraction(1,1),
			 code={"fraction/fraction":"LHO=subtract_fractions(LHO,RHO)"}),
	Operator("lick", "add",
			 grammar=["have", "plain"],
			 default=Fraction(1,1),
			 code={"fraction/fraction": "LHO=add_fractions(LHO,RHO)"}),
	Operator("worship", "multiply",
			 grammar=["have", "plain"],
			 default=Fraction(1, 1),
			 code={"fraction/fraction": "LHO=multiply_fractions(LHO,RHO)"}),
	Operator("moan", "assign",
			 alt="beg",
			 grammar=["make"],
			 default="",
			 code={"fraction/fraction": "LHO=RHO",
				   "fraction/chain": "LHO=chain_to_fraction(RHO)",
				   "chain/fraction": "clear_chain(&LHO);append_fraction_to_chain(&LHO, RHO)",
				   "chain/chain": "clear_chain(&LHO);append_chain_to_chain(&LHO, RHO)"
				   }),
	Operator("scream", "assign_with_newline",
			 alt="plead",
			 grammar=["make"],
			 default="",
			 code={
				   "chain/fraction": 'clear_chain(&LHO);append_fraction_to_chain(&LHO,RHO);append_cstr_to_chain(&LHO,"\\n")',
				   "chain/chain": 'clear_chain(&LHO);append_chain_to_chain(&LHO, RHO);append_cstr_to_chain(&LHO,"\\n")'
				   }),
	Operator("tie up", "concat",
			 grammar=["have"],
			 default=None,
			 code={
				 "chain/fraction": "append_fraction_to_chain(&LHO, RHO)",
				 "chain/chain": "append_chain_to_chain(&LHO, RHO)"
			 })

]

# Comparison operators
comparison_operators = [
	Operator("is", "==",
			 code={
				 "fraction/fraction": "(compare_fractions(LHO, RHO)==0)",
				 "chain/chain": "(compare_chains(LHO, RHO)==0)"
			 }),
	Operator("is not", "!=",
			 alt="isn't",
			 code={
				"fraction/fraction": "(compare_fractions(LHO, RHO)!=0)",
				 "chain/chain": "(compare_chains(LHO, RHO)!=0)"
			 }),
	Operator("is over", ">",
			 alt="isn't",
			 code={
				 "fraction/fraction": "(compare_fractions(LHO, RHO)==1)",
			 }),
	Operator("is under", "<",
			 alt="isn't",
			 code={
				 "fraction/fraction": "(compare_fractions(LHO, RHO)==-1)",
			 }),
	Operator("is dominant towards", ">=",
			 alt="isn't",
			 code={
				 "fraction/fraction": "(compare_fractions(LHO, RHO)>=0)",
			 }),
	Operator("is submissive towards", "<=",
			 alt="isn't",
			 code={
				 "fraction/fraction": "(compare_fractions(LHO, RHO)<=0)",
			 })
]
