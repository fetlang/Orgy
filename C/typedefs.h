#ifndef ORGY_TYPEDEFS_H_
#    define ORGY_TYPEDEFS_H_
#    include <stdint.h>
#    include <inttypes.h>
/* Fraction Int Definition */
typedef int64_t FractionInt;

/* Fraction Int Formatter for Printf
   Because I shouldn't have to consider the
   fact that it's 64 bits in other code in
   case I want to change it
*/
#    define FRACTION_INT_FORMATTER PRId64

/* Type for chain length. The max of this is the max size of a chain */
typedef unsigned int ChainLengthInt;
#endif
