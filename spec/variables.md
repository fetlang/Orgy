## Tokenizing
Variables are case insensitive. Any character, but limited to,
that is alphanumeric, an underscore, a hyphen, or a space may be used.
Tokenization ends at a newline, a reserved word, or the start of a
literal.

Identifiers expressing possession are the same as their possessor. For
example:

`Richard Stallman's sexy feet` is the same as `riCHard StallMAN`

## Permissions
Variables have two permissions: reading and writing  
The programmer cannot restrict these, but some builtin variables might
be restricted, like mathematical constants or STDIN/STDOUT/STDERR

## Types
The type of a variable is implied by the first operation it is in. If it
is in a situation in which it could either be a fraction or chain, it
will default to chain.  

To see types, see `types.md`

## Gender
Variables can be assigned one of four genders: male, female, neutral,
 and nonperson. Additionally, an N/A (not applicable) gender exists, but
 cannot be assigned to a variable by the programmer. No variable starts
 with a gender (that is, they start with `None`), but once a gender is
assigned, it cannot be changed.  

Each gender is associated with a pair of pronouns:  
Male - `HIM`/`HIMSELF`/`HIS`  
Female - `HER`/`HERSELF`/`HER`  
Neutral - `THEY`/`THEMSELF`/`THEIR`  
Nonperson - `IT`/`ITSELF`/`ITS`

Male, female, and neutral are reserved for human-ly named variables,
like `Sasha Grey`  
Nonperson is reserved for object-ly named variables, like `violet wand`
N/A is reserved for non-nouns, like the `NAUGHTY`


## Pronouns
Using a pronoun to describe a variable will imply its gender if it does
not have one yet. Use of an objective pronoun will use the last variable
mentioned that is not in the left-sided operand (not LHO). Use of a
reflexive pronoun will use the variable used in the left-sided operand
(if it cannot, compilation will fail). Use of possesive pronouns act the
same way as possesive variables.

Examples:

Subtract `Richard Stallman`(male) from `Richard Stallman`:
    
    Have Richard Stallman spank himself

Subtract `Rufus Xavier Sarsaparilla` from `Ada Lovelace`
Multiply `Ada Lovelace`(female) by `Linus Torvalds`(no gender):

    Have Rufus Xavier Sarsaparilla spank Ada Lovelace
    Have Linus Torvalds worship her feet

Add `Guido Van Rossum`(male) to `Guido Van Rossum`

    Have Guido Van Rossum lick his own cock
