#include <stdlib.h>
#include <stdio.h>
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
		it = it->next;
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
		it = it->next;
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

Fraction chain_min(Chain chain){
	Fraction min;
	Link* it;

	/* Raise error if needed */
	if(chain.length == 0){
		runtime_error("cannot find minimum of an empty chain");
	}

	it = chain.start;
	min= it -> value;

	while(it -> next != NULL){
		it = it->next;
		min = compare_fractions(min, it->value) == -1 ? min : it->value;
	}

	return min;
}

Fraction chain_stddev(Chain chain){
    Fraction mean;
    Fraction length;
    Fraction dev;
    Fraction temp;
    Fraction exponent;
    Link * it;

    /* Get mean */
    mean = chain_mean(chain);
    printf("Mean: %ji/%ji\n", mean.num, mean.den);
    /* Get length */
    length.num = chain.length;
    length.den = 1;

    /* Set exponent to 2 */
    exponent.num = 2;
    exponent.den = 1;

    /* Sum up (x-mean)^2 */
    it = chain.start;
    dev.num = 0;
    dev.den = 1;
    while(it != NULL){
        /* Calculate (x-mean)^2 */
        temp = it->value;
        temp = subtract_fractions(temp, mean);
        temp = pow_fractions(temp, exponent);
        printf("(x-mean)^2: %ji/%ji\n", temp.num, temp.den);

        /* Add to  sum*/
        dev = add_fractions(dev, temp);

        /* Forward iterator */
        it = it->next;
    }

    /* Divide by length */
    printf("Sum: %ji/%ji\n", dev.num, dev.den);
    length.num -= 1;
    dev = divide_fractions(dev, length);
    printf("sd^2 %ji/%ji\n", dev.num, dev.den);

    /* Take square root */
    exponent.num = 1;
    exponent.den = 2;
    dev = pow_fractions(dev, exponent);
    printf("stddev: %ji/%ji\n", dev.num, dev.den);
    return dev;
}
