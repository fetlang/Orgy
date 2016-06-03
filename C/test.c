#include "fraction_math.h"
#include "chain.h"
#include <stdio.h>
int main()
{

	Chain a;
	Chain b;
	printf("Chain Test\n");
	init_chain(&a);
	init_chain(&b);
	append_cstr_to_chain(&a, "I'm like a porno star,\0");
	append_cstr_to_chain(&b, " I come so hard\0");
	append_cstr_to_chain(&b, ". I can't go back to my virginity\n");
	append_chain_to_chain(&a, b);
	print_chain(a);
	print_chain(b);
	clear_chain(&a);
	clear_chain(&b);
	{

		Fraction a;
		Fraction b;
		Fraction* c;
		printf("Fraction Test (exp)\n");
		a.num = 50;
		a.den = 1;
		b.num = 3;
		b.den = 5;
		*c = exponentiate_fractions(a, b);
		printf("%i/%i\n", c->num, c->den);

	}
	return 0;
}
