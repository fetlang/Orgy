## Operator Grammar
#### Plain Grammar
&lt;operator&gt; LHO  
&lt;operator&gt; LHO &lt;fraction literal&gt; times
#### Make Grammar
MAKE LHO &lt;operator&gt;  
MAKE LHO &lt;operator&gt; &lt;chain literal&gt;  
MAKE LHO &lt;operator&gt; RHO  
#### Have Grammer
HAVE RHO &lt;operator&gt; LHO  

## Operators
#### SPANK
Grammar: have, plain
Default: 1/1

    Subtract(Fraction& LHO, Fraction RHO)  
#### LICK
Grammar: have, plain
Default: 1/1

    Add(Fraction& LHO, Fraction RHO)
#### WORSHIP
Grammar: have, plain
Default: 1/1

    Multiply(Fraction& LHO, Fraction RHO)
#### HUMILIATE
Grammar: have, plain
Default: 1/1

    Divide(Fraction& LHO, Fraction RHO)  
#### SUCK
Grammar: have, plain
Default: 1/1

    Modulus(Fraction& LHO, Fraction RHO)  
#### TICKLE
Grammar: have, plain
Default: 1/1

    Exponent(Fraction& LHO, Fraction RHO)  
#### MOAN/BEG
Grammar: make
Default: ""

    /* Assign value of RHO to LHO */
    Assign(Fraction& LHO, Fraction RHO)
    Assign(Chain& LHO, Chain RHO)
    
    /* Convert RHO to chain, and assign to LHO */
    Assign(Chain& LHO, Fraction RHO)
    
    /* Convert RHO to Fraction, and assign to LHO */
    Assign(Fraction& LHO, Chain RHO)
    

#### SCREAM/PLEAD
Grammar: make
Default: ""

    /* Assign value of RHO to LHO */
    Assign_plus_newline(Chain& LHO, Chain RHO)
    
    /* Convert RHO to chain, and assign to LHO */
    Assign_plus_newline(Chain& LHO, Fraction RHO)

#### TIE UP
Grammar: have
Default: None

    Concat(Chain& LHO, Chain RHO)
    Concat(Chain& LHO, Fraction RHO) 

