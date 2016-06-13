## Fractions
All numbers in Orgy are represented as fractions: a numerator over a
denominator.

## Chains
Chains are lists of fractions. They can be used as strings, or just an
array of numbers. When printed as a string, each fraction is converted
into an ASCII code.

## Streams
Streams are treated like chains in Orgy, but have limitations. The three
stream types are: stdout, stdin, and stderr. Stdout and stderr can only
be used as reference chains. Stdin can only be used as non-reference
chains. Stdout and Stdin are referred to by named variables, as shown in
`builtins.md`