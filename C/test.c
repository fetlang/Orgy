#include "fraction_math.h"
#include "chain.h"
#include "chain_math.h"
#include <stdio.h>
int main()
{

	Chain a;
	Fraction b;
	init_chain(&a);

	b.num = 3;
	b.den = 1;

	append_flink_to_chain(&a, b);


	b.num = 5;
	b.den = 1;

	append_flink_to_chain(&a, b);

	b.num = 11;
	b.den = 2;

	append_flink_to_chain(&a, b);
	print_chain_numerically(a);
	printf("\nCalculating standard deviation\n");
	b = chain_stdev(a);


	printf("stdev:%" FRACTION_INT_FORMATTER "/%" FRACTION_INT_FORMATTER
	       "\n", b.num, b.den);

	return 0;
}
