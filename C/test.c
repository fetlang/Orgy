#include "fraction_math.h"
#include "chain.h"
#include "chain_math.h"
#include <stdio.h>
int main()
{
	Chain a;
	init_chain(&a);
	append_fraction_to_chain(&a, construct_fraction(-100, 100));
	chain_to_stream(a, stdout);





	return 0;
}
