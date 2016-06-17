#include "compatibility.h"
#include "fraction_math.h"
#include "chain.h"
#include "chain_math.h"
#include <stdio.h>
int main()
{
	Chain a;
	Fraction b;
	init_chain(&a);
	while(1){
		clear_chain(&a);
		append_stream_to_chain(&a, stdin);
		b = chain_to_fraction(a);
		append_fraction_to_chain(&a, b);
		chain_to_stream(a, stdout);
		putchar(10);
	}





	return 0;
}
