#ifndef ORGY_FRACTION_H_
#define ORGY_FRACTION_H_
#include "typedefs.h"

/* Fraction structure for Orgy */
typedef struct OrgyFractionStructure {
	FractionInt num;	/* numerator */
	FractionInt den;	/* denominator */
} Fraction;

/* Fake constructor for Fraction */
Fraction construct_fraction(FractionInt num, FractionInt den);
#endif
