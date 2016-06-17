/* Indicate lack of support for ANSI C

Orgy Support:
	C99 and higher
	C++98 and higher
*/
#ifndef __cplusplus
#if __STDC_VERSION__ < 199901L
#error Language not supported. Please use C99 or higher, or C++98 or higher
#endif
#endif