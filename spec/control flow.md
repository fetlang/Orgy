## Comparison operators
`IS` - `==`  
`IS NOT`/`ISN'T` - `!=`  
`IS OVER` - `>`  
`IS UNDER` - `<`  
`IS SUBMISSIVE TOWARDS` - `>=`  
`IS DOMINANT TOWARDS` - `<=`  

## `IF` statements
    IF <lho> [COMPARISON] <rho>
    ...
    END IF

## `WHILE`/`UNTIL` loops

    [WHILE | UNTIL] <lho> [COMPARISON] <rho>
    ...
    MORE PLEASE

## Safewords
Safewords allow you to exit a scope prematurely. It is 

`DECLARE` can only be used in the global scope. `WITH` can only be used after an a line
containing `IF`, `WHILE`, or `UNTIL`

    DECLARE SAFEWORD <safeword>
    ...
    [<safeword>]
fafsfd

    [IF | WHILE | UNTIL] <lho> [COMPARISON] <rho>
    WITH SAFEWORD <safeword>
    ...
    [<safeword>]
