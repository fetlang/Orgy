#include "fraction_math.h"
#include "error.h"
#include <math.h>

static void reduce_fraction(Fraction* a){
	/* Check for negative error*/
	if(a->den<0){
		runtime_error("negative denominator (this shouldn't happen)");
	}
	
	/* Don't divide by zero*/
	if (a->den==0){
		if(a->num==0)
			runtime_error("division of zero by zero");
		return;
	}
	
	/* Reduce if numerator is multiple of denominator*/
	if(a->num%a->den==0){
		a->num/=a->den;
		a->den=1;
		return;
	}
	
	/* Get maximum */
	uint64_t max = sqrt(abs(a->num)<a->den?a->num:a->den)+1;
	uint64_t c;

	/* Reduce by 2*/
	while (a->num%2 == 0 && a->den%2 == 0){
		a->num /= 2;
		a->den /= 2;
	}

	/* Reduce by odd numbers*/
	for(c=3; c < max;c+=2){
		while (a->num%c == 0 && a->den%c ==0){
			a->num /= c;
			a->den /=c;
		}
	}
	
}

Fraction add_fractions(Fraction a, Fraction b){
	Fraction new_frac;
	/* Add fractions with different denominators*/
	if(a.den!=b.den){
		new_frac.num = a.num * b.den + b.num*a.den;
		new_frac.den = a.den * b.den;
	/* Add fractions with different denominators*/
	}else{
		new_frac.num = a.num + b.num;
		new_frac.den = a.den;
	}
	/* Reduce and return*/
	reduce_fraction(&new_frac);
	return new_frac;
}

Fraction subtract_fractions(Fraction a, Fraction b){
	/* Just add a negative fraction*/
	b.num = -b.num;
	return add_fractions(a,b);
}

Fraction multiply_fractions(Fraction a, Fraction b){
	a.num*=b.num;
	a.den*=b.den;
	reduce_fraction(&a);
	return a;
}

Fraction divide_fractions(Fraction a, Fraction b){
	a.num*=b.den;
	a.den*=b.num;
	reduce_fraction(&a);
	return a;
}

Fraction modulus_fractions(Fraction a, Fraction b){
	if(a.den!=1 || b.den!=1){
		runtime_error("cannot mod non-integers");
	}
	a.num%=b.num;
	reduce_fraction(&a);
	return a;
}