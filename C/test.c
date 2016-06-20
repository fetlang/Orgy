#include "compatibility.h"
#include "fraction_math.h"
#include "chain.h"
#include "chain_math.h"
#include <stdio.h>
int main()
{
	/* Define chains */
	Chain a;
	Fraction b;
	init_chain(&a);

	/* Start loop */
	while (1) {
		/* Delete chain */
		clear_chain(&a);

		/* Take input and convert to fraction */
		append_stream_to_chain(&a, stdin);
		b = chain_to_fraction(a);

		/* Clear chain and append fraction to it */
		clear_chain(&a);
		append_fraction_to_chain(&a, b);

		/* Print out chain + '\n' */
		chain_to_stream(a, stdout);
		printf("\n\n");
	}





	return 0;
}
