#include "chain.h"
#include "error.h"
#include "fraction_math.h"
#include <tgmath.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void init_chain(Chain * chain)
{
	chain->length = 0;
	chain->start = NULL;
	chain->end = NULL;
}

void clear_chain(Chain * chain)
{
	/* Make pointer to first link */
	Link *temp = chain->start;

	/* If it's null, it's already cleared(hopefully) */
	if (chain->start == NULL)
		return;

	/* Free all except the last link */
	while (temp->next != NULL) {
		temp = temp->next;
		free(temp->prev);
	}

	/* Free last link */
	free(temp);

	/* Reset chain */
	chain->length = 0;
	chain->start = NULL;
	chain->end = NULL;
}

void append_cstr_to_chain(Chain * chain, const char *text)
{
	unsigned int k;
	for (k = 0; text[k] != '\0'; k++) {
		append_flink_to_chain(chain,
				      construct_fraction((FractionInt)
							 text[k], 1));
	}

}

void append_flink_to_chain(Chain * chain, Fraction fraction)
{
	/* Create new link */
	Link *new_link = (Link *) malloc(sizeof(Link));
	new_link->value = fraction;

	/* Insert at end */
	new_link->prev = chain->end;
	new_link->next = NULL;
	if (chain->start == NULL) {
		chain->start = new_link;
	} else {
		chain->end->next = new_link;
	}
	chain->end = new_link;

	/* Increment length */
	chain->length++;
}

void append_chain_to_chain(Chain * chain1, Chain chain2)
{
	Link *it = chain2.start;
	if (it == NULL) {
		return;
	}
	if (chain1->start == NULL) {
		/* Set up iterator as first node */
		chain1->start = (Link *) malloc(sizeof(Link));
		chain1->start->value = it->value;
		chain1->start->prev = NULL;
		chain1->start->next = NULL;
		chain1->end = chain1->start;
	} else {
		/* Set up iterator at end */
		chain1->end->next = (Link *) malloc(sizeof(Link));
		chain1->end->next->prev = chain1->end;
		chain1->end->next->next = NULL;
		chain1->end = chain1->end->next;
		chain1->end->value = it->value;
	}
	while (it->next != NULL) {
		/* Forward iterator */
		it = it->next;
		/* Add node at end */
		chain1->end->next = (Link *) malloc(sizeof(Link));
		chain1->end->next->prev = chain1->end;
		chain1->end->next->next = NULL;
		chain1->end = chain1->end->next;
		chain1->end->value = it->value;
	}

	/* Increment length */
	chain1->length += chain2.length;

}

void chain_to_stream(Chain chain, FILE * stream)
{
	/* Iterator */
	Link *it = chain.start;

	/* Print out chain */
	while (it != NULL) {
		/* Print character */
		fprintf(stream, "%c",(char) (it->value.num / it->value.den));
		
		/* Forward iterator */
		it = it->next;
	}
}

void append_stream_to_chain(Chain * chain, FILE * stream)
{
	/* Initiate character to something not important */
	char character = 'T';

	/* While not end of file or end of line */
	while (character != '\n' && character != EOF) {

		/* Get character from stream */
		character = (char) fgetc(stream);

		/* Append to chain */
		append_flink_to_chain(chain,
				      construct_fraction((FractionInt)
							 character, 1));
	}
}

static void num_to_cstr(char *str, FractionInt num)
{
	/* List numeric literals */
	char *zero_to_nineteen[] = {
		"zero", "one", "two", "three", "four", "five", "six",
		"seven", "eight", "nine", "ten", "eleven",
		"twelve", "thirteen", "fourteen", "fifteen", "sixteen",
		"seventeen", "eighteen", "nineteen"
	};
	char *twenty_to_ninety[] =
	    { "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
		"eighty", "ninety"
	};
	char *big_numbers[] =
	    { "thousand", "million", "billion", "quadrillion",
  "quintillion" };

	/* Check for less-than-zero error */
	if (num < 0) {
		runtime_error
		    ("num is less than zero in num_to_cstr(this shouldn't happen)");
	} else
		/* Singles and teens */
	if (num < 20) {
		strcpy(str, zero_to_nineteen[num]);
	} else
		/* Adults */
	if (num % 10 == 0 && num < 100) {
		strcpy(str, twenty_to_ninety[num / 10 - 2]);
	} else
		/* Mature */
	if (num % 1000 == 0) {
		strcpy(str, big_numbers[(FractionInt) log10(num) / 3 - 1]);
		/* Anything else returns an error */
	} else {
		runtime_error
		    ("num not valid for num_to_cstr(this shouldn't happen)");
	}
}

static void append_triple_to_chain(Chain * chain, FractionInt triple)
{
	char temp[50];
	/* Error if triple is too big or too small */
	if (triple > 999 || triple < 0) {
		runtime_error("invalid triple (you should not see this)");
	}

	/* 100's place */
	if (triple / 100 != 0) {
		num_to_cstr(temp, triple / 100);
		append_cstr_to_chain(chain, temp);
		append_cstr_to_chain(chain, " hundred");
		triple %= 100;
		if (triple != 0) {
			append_cstr_to_chain(chain, " and ");
		} else {
			return;
		}

	}


	/* Tens place */
	if (triple / 10 != 0 && triple > 20) {
		num_to_cstr(temp, (triple / 10) * 10);
		append_cstr_to_chain(chain, temp);
		triple %= 10;
		if (triple != 0) {
			append_cstr_to_chain(chain, " ");
		} else {
			return;
		}
	}

	/* Ones place */
	if (triple) {
		num_to_cstr(temp, triple);
		append_cstr_to_chain(chain, temp);
	}

}

static void append_fraction_int_to_chain(Chain * chain, FractionInt num)
{
	FractionInt magnitude = 0;
	int started = 0;
	char temp[50];

	/* Find magnitude */
	for (magnitude = 1; (num / magnitude) != 0; magnitude *= 1000);

	/* Write to chain */
	while (magnitude > 0) {
		/* If applicable... */
		if (num / magnitude != 0) {
			/* Add space */
			if (started == 1) {
				append_cstr_to_chain(chain, ", ");
			} else {
				started = 1;
			}

			/* Add triple to chain */
			append_triple_to_chain(chain, num / magnitude);

			/* If in 1000's, million's, etc's place ... */
			if (magnitude != 1) {
				/* Append a space, and an appropriate power-of-thousand modifier */
				append_cstr_to_chain(chain, " ");
				num_to_cstr(temp, magnitude);
				append_cstr_to_chain(chain, temp);
			}
		}

		/* Reduce number and magnitude */
		num -= (num / magnitude) * magnitude;
		magnitude /= 1000;
	}
}

void append_fraction_to_chain(Chain * chain, Fraction fraction)
{
	/* Reduce fraction */
	reduce_fraction(&fraction);
	
	/* Append "negative" if necessary */
	if (fraction.num < 0) {
		append_cstr_to_chain(chain, "negative ");
		/* Make numerator positive */
		fraction.num = -fraction.num;
		/* Check if zero */
	} else if (fraction.num == 0) {
		append_cstr_to_chain(chain, "zero");
		return;
	}
	/* Check if infinity */
	if (fraction.den == 0) {
		append_cstr_to_chain(chain, "infinity");
		return;
	}


	/* Write numerator to chain */
	append_fraction_int_to_chain(chain, fraction.num);
	
	/* Write denominator to chain */
	if(fraction.den != 1){
		append_cstr_to_chain(chain, " over ");
		append_fraction_int_to_chain(chain, fraction.den);
	}
}


void print_chain_numerically(Chain chain)
{
	Link *it = chain.start;
	printf("(");
	while (it != NULL) {
		/* Display item numerator as integer */
		printf("%s%" FRACTION_INT_FORMATTER,
		       it != chain.start ? ", " : "", it->value.num);

		/* Display denominator if not 1 */
		if (it->value.den != 1) {
			printf("/%" FRACTION_INT_FORMATTER, it->value.den);
		}

		/* Forward iterator */
		it = it->next;
	}
	printf(")");
}
