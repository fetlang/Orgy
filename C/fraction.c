#include "fraction.h"

Fraction construct_fraction(FractionInt num, FractionInt den)
{
	Fraction frac;
	frac.num = num;
	frac.den = den;
	return frac;
}
