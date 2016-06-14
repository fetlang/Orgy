## `IF` statements
    IF <lho> [IS | IS OVER | IS UNDER] <gho>
    ...
    END IF

## `WHILE`/`UNTIL` loops

    [WHILE | UNTIL] <lho> [IS | IS OVER | IS UNDER] <gho>
    ...
    MORE PLEASE

## Safewords
Safewords allow you to exit a scope prematurely.  

`DECLARE` can be used anywhere. `WITH` can only be used after an a line
containing `IF`, `WHILE`, or `UNTIL`

    [DECLARE|WITH] SAFEWORD <safeword>
    ...
    [<safeword>]
