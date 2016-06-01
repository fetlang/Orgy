#include "fraction_math.h"
#include "chain.h"
#include <stdio.h>
int main()
{
	Chain chain;
	init_chain(&chain);
	append_cstr_to_chain(&chain,
			     "Bless my soul, Herc was on a role\0");
	print_chain(chain);
	clear_chain(&chain);
	return 0;
}
