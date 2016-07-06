import parser
import lexer


class Transpiler:
	def __init__(self, ocode):
		lex = lexer.Lexer(ocode)
		self.tree = parser.Parser(lex.tokens).tree.children

		self.ccode="""#include "compatibility.h"
#include "fraction_math.h"
#include "chain.h"
#include "chain_math.h"
#include <stdio.h>
int main(){
Chain WRITING_BUFFER;
init_chain(&WRITING_BUFFER);
CHAIN READING_BUFFER;
init_chain(&READING_BUFFER);
"""

	# Recursively traverse tree
	def _transpile(self, root):
		for child in root.children:
			if child.kind == "operator":
				code_lookup = child.children[0].

Transpiler("""GAG
	This is a sample program
	UNGAG

	Lick Carl
	Lick Jenny
	until Jenny is over forty
		have Jenny lick Carl's dick
		have Carl worship her feet
	more please
	""")
