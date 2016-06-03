#include "chain_math.h"
#include "fraction_math.h"
#include "error.h"

Fraction chain_sum(Chain chain)
{
	/* Declare iterator */
	Link *it = chain.start;

	/* Declare sum and initiate it to zero */
	Fraction sum;
	sum.num = 0;
	sum.den = 1;

	/* Compute sum */
	while (it != NULL) {
		sum = add_fractions(sum, it->value);
	}

	/* Return sum */
	return sum;
}

Fraction chain_product(Chain chain)
{
	/* Declare iterator */
	Link *it = chain.start;

	/* Declare product and initiate it to one */
	Fraction product;
	product.num = 1;
	product.den = 1;

	/* Compute product */
	while (it != NULL) {
		product = multiply_fractions(product, it->value);
	}

	/* Return sum */
	return product;
}

Fraction chain_mean(Chain chain)
{
	/* Get length as fraction */
	Fraction length;
	length.num = chain.length;
	length.den = 1;

	/* Return sum divided by length */
	return divide_fractions(chain_sum(chain), length);
}

Fraction chain_max(Chain chain){
	Fraction max;
	Link* it;

	/* Raise error if needed */
	if(chain.length == 0){
		runtime_error("cannot find maximum of an empty chain");
	}

	it = chain.start;
	max = it -> value;

	while(it -> next != NULL){
		it = it->next;
		max = compare_fractions(max, it->value) != -1 ? max : it->value;
	}

	return max;
}