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
	unsigned int k = 0;
	for (; text[k] != '\0'; k++) {
		/* Make new link */
		Link *new_link = (Link *) malloc(sizeof(Link));
		new_link->next = NULL;
		new_link->prev = it;
		new_link->value = text[k];

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

void print_chain(Chain chain)
{
	Link *it = chain.start;
	while (it != NULL) {
		putchar(it->value);
		it = it->next;
	}
}
