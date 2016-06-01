#ifndef ORGY_CHAIN_H_
#    define ORGY_CHAIN_H_
/* Chains (strings) are represented as linked lists*/
typedef struct Link {
	char value;
	struct Link *prev;	/* Starts at NULL */
	struct Link *next;	/* Ends at NULL */
} Link;
typedef struct OrgyChainStructure {
	unsigned int length;
	Link *start;
	Link *end;
} Chain;

/* Set defaults for chain, length to 0 and start to NULL*/
void init_chain(Chain * chain);

/* Delete all links in chain and set start to NULL */
void clear_chain(Chain * chain);

/* Concat a cstring to a chain*/
void append_cstr_to_chain(Chain * chain, const char *text);

/* Traverse chain and print each value*/
void print_chain(Chain chain);
#endif
