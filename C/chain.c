#include "chain.h"
#include <stdlib.h>
#include <stdio.h>

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
	/* Iterator go to end of chain */
	Link *it = chain->end;

	/* Go through text */
	ChainLengthInt k = 0;
	for (; text[k] != '\0'; k++) {
		/* Make new link */
		Link *new_link = (Link *) malloc(sizeof(Link));
		new_link->next = NULL;
		new_link->prev = it;
		new_link->value.num = (FractionInt) text[k];
		new_link->value.den = 1;

		/* Increment length */
		chain->length++;

		/* Connect iterated node to new link */
		if (it == NULL) {
			chain->start = new_link;
			chain->end = new_link;
		} else {
			it->next = new_link;
			chain->end = new_link;
		}
		it = new_link;
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

void print_chain(Chain chain)
{
	Link *it = chain.start;
	while (it != NULL) {
		/* Display item as character */
		putchar((char) (it->value.num / it->value.den));

		/* Forward iterator */
		it = it->next;
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
