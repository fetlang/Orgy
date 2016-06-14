## Fractions
All numbers in Orgy are represented as fractions: a numerator over a
denominator.

Fraction literals are represented by words. For example, -45153/71 is
represented by:

    negative forty-five thousand one hundred and fifty-three over
    seventy-one

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
Streams are treated like chains in Orgy, but have limitations. The three
stream types are: stdout, stdin, and stderr. Stdout and stderr can only
be used as reference chains. Stdin can only be used as non-reference
chains. Stdout and stdin are referred to by named variables, as shown in
`builtins.md`
