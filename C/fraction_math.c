#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include "fraction_math.h"
#include "error.h"
#if __STDC_VERSION__ >= 199901L
#define abs llabs
#define pow powl
#define long_double long double
#else
#define abs labs
#define long_double double
#endif




static void reduce_fraction(Fraction * a)
{
	FractionInt max;
	FractionInt c;


	/* Check for negative error */
	if (a->den < 0) {
		runtime_error
		    ("negative denominator (this shouldn't happen)");
	}

	/* Don't divide by zero */
	if (a->den == 0) {
		if (a->num == 0)
			runtime_error("division of zero by zero");
		return;
	}

	/* Reduce if numerator is multiple of denominator */
	if (a->num % a->den == 0) {
		a->num /= a->den;
		a->den = 1;
		return;
	}

	/* Get maximum */
	max = sqrt(abs(a->num) < a->den ? a->num : a->den) + 1;

	/* Reduce by 2 */
	while (a->num % 2 == 0 && a->den % 2 == 0) {
		a->num /= 2;
		a->den /= 2;
	}

	/* Reduce by odd numbers */
	for (c = 3; c < max; c += 2) {
		while (((a->num % c) == 0) && ((a->den % c) == 0)) {
			a->num /= c;
			a->den /= c;
		}
	}

}

Fraction add_fractions(Fraction a, Fraction b)
{
	Fraction new_frac;

	/* Add fractions with different denominators */
	new_frac.num = a.num * b.den + b.num * a.den;
	new_frac.den = a.den * b.den;

	/* Reduce and return */
	reduce_fraction(&new_frac);
	return new_frac;
}

Fraction subtract_fractions(Fraction a, Fraction b)
{
	/* Just add a negative fraction */
	b.num = -b.num;
	return add_fractions(a, b);
}

Fraction multiply_fractions(Fraction a, Fraction b)
{
	/* Multiply numerator to numerator and denominator to denominator */
	a.num *= b.num;
	a.den *= b.den;
	reduce_fraction(&a);
	return a;
}

Fraction divide_fractions(Fraction a, Fraction b)
{
	/* Multiply numerator with denominator and denominator with numerator */
	a.num *= b.den;
	a.den *= b.num;
	reduce_fraction(&a);
	return a;
}

Fraction modulus_fractions(Fraction a, Fraction b)
{
	if (a.den != 1 || b.den != 1) {
		runtime_error("cannot mod non-integers");
	}
	a.num %= b.num;
	reduce_fraction(&a);
	return a;
}

Fraction pow_fractions(Fraction a, Fraction b)
{
	int reverse = 0;
	FractionInt i = 0;
	Fraction temp;

    /* Increase accuracy */
    if(a.den > 1){
        a.num *= 256;
        a.den *= 256;
    }

	/* Check for 0^0 error */
	if((a.num == 0 || a.den ==0) && (b.num == 0 || b.num == 0)){
		runtime_error("cannot exponentiate zero or infinity to zero or infinity");
	}

	/* Check if inverse needs to be took */
	if (b.num < 0) {
		reverse = 1;
		b.num = -b.num;
	}

	/* Exponentiate a's numerator with b's numerator */
	temp = a;
	a.num = 1;
	a.den = 1;
	for (i = 0; i < b.num; i++) {
		a.num *= temp.num;
		a.den *= temp.den;
	}

	/* Check if a's num can't be rooted by b's denominator */
	if (a.num < 0 && b.den % 2 == 0) {
		runtime_error
		    ("cannot take even-number root of a negative number");
	}

	/* Root a */
	if(b.den != 1){
        a.num = (FractionInt) pow((long_double) a.num, 1 / ((long_double) b.den));
        a.den = (FractionInt) pow((long_double) a.den, 1 / ((long_double) b.den));
	}

	/* Reduce, and inverse if necessary */
	if (reverse) {
		i = a.den;
		a.den = a.num;
		a.num = i;
	}
	reduce_fraction(&a);
	return a;
}

int compare_fractions(Fraction a, Fraction b){
	/* If whole numbers or infinities, just compare numerators */
	if((a.den == 1 && b.den == 1) || (a.den==0 && b.den==0)){
		return a.num>b.num?1:a.num<b.num?-1:0;
	}

	/* Infinitite number vs finite number */
	if(a.den == 0){
		return a.num > 0 ? 1 : -1;
	}
	if(b.den == 0){
		return b.num > 0 ? -1 : 1;
	}

	/* Everything else */
	return a.num * b.den > b.num * a.den ? 1 : a.num * b.den < b.num * a.den ? -1 : 0;
}
