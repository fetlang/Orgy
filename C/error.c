#include <stdio.h>
#include <stdlib.h>
#include "error.h"

void runtime_error(const char *msg)
{
	fprintf(stderr, "runtime error: %s\n", msg);
	exit(EXIT_FAILURE);
}
