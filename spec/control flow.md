## Comparison operators
<<<<<<< HEAD
`IS` - `==`  
`IS NOT`/`ISN'T` - `!=`  
`IS OVER` - `>`  
`IS UNDER` - `<`  
`IS SUBMISSIVE TOWARDS` - `>=`  
`IS DOMINANT TOWARDS` - `<=`  
=======
`IS` - `==`
`IS NOT`/`ISN'T` - `!=`
`IS OVER` - `>`
`IS UNDER` - `<`
`IS SUBMISSIVE TOWARDS` - `>=`
`IS DOMINANT TOWARDS` - `<=`
>>>>>>> f780df3d4b88c17a5a47700890b9c6077db1a71c


## `IF` statements
    IF <lho> [COMPARISON] <rho>
    ...
    END IF

## `WHILE`/`UNTIL` loops

    [WHILE | UNTIL] <lho> [COMPARISON] <rho>
    ...
    MORE PLEASE

## Safewords
Safewords allow you to exit a scope prematurely.

`DECLARE` can be used anywhere. `WITH` can only be used after an a line
containing `IF`, `WHILE`, or `UNTIL`

    [DECLARE|WITH] SAFEWORD <safeword>
    ...
    [<safeword>]
