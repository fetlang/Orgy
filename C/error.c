#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include "error.h"

/* Allow for red, bold highlighting on UNIX systems */
#ifdef __unix__
#define HIGHLIGHT "\x1B[1;31m"
#define DEHIGHLIGHT "\x1B[0m"
#else
#define HIGHLIGHT ""
#define DEHIGHLIGHT ""
#endif

void runtime_error(const char *msg, ...)
{
	va_list args;

	/* Error header */
	fprintf(stderr, HIGHLIGHT "runtime error:" DEHIGHLIGHT " ");

	/* Print msg and args to stderr, printf style */
	va_start(args, msg);
	vfprintf(stderr, msg, args);
	va_end(args);

	/* New line and exit */
	fprintf(stderr, "\n");
	exit(EXIT_FAILURE);
}
