#include "fraction_math.h"
#include <stdio.h>
int main(){
	Fraction a;
	a.num = 9;
	a.den = 1;
	a = add_fractions(a,a);
	printf("%i/%i\n", a.num,a.den);
return 0;
}