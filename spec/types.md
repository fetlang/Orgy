## Fractions
All numbers in Orgy are represented as fractions: a numerator over a
denominator.

Fraction literals are represented by words. For example, -45153/71 is
represented by:

    negative forty five thousand one hundred and fifty three over
    seventy one

When printed to stdout, fractions are written with commas:

    negative forty five thousand, one hundred and fifty three over
    seventy one

When read from stdin, fractions are inputed as:

    -45153/71

Normally, 0/0 is not allowed, but when inputed by the user it is equal
to 1/1.

## Special Fractions
Some fractions aren't really fractions. The Orgy wrappers for the C
functions rand() and time(NULL) have identifiers named in `builtins.md`
and are treated just like fractions, but are read only.


## Chains
Chains are lists of fractions. They can be used as strings, or just an
array of numbers. When printed as a string, each fraction is converted
into an ASCII code.

Chain literals are the same as C `char*` literals:

    "Hello World!\n"

Chain literals cannot be concatenated by placing them next to each
other, and multi-line chain literals cannot exist.

Chains are not null-terminated.


## Streams
Streams are treated like chains in Orgy. The three stream types are:
stdout, stdin, and stderr. Stdout and stdin are referred to by identifiers
as shown in `builtins.md`

A stream can be used in place of a chain variable, any time.
