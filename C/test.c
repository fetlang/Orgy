#include "fraction_math.h"
#include "chain.h"
#include "chain_math.h"
#include <stdio.h>
int main()
{

	Chain a;
	init_chain(&a);
	append_cstr_to_chain(&a, "Hello World!\n");
	chain_to_stream(a, stdout);
	

	return 0;
}
