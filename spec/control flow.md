## `if` statements
    IF <lho> [IS | IS OVER | IS UNDER] <gho>
    ...
    END IF

## `while`/`until` loops

    [WHILE | UNTIL] <lho> [IS | IS OVER | IS UNDER] <gho>
    ...
    MORE PLEASE

## Safewords
Safewords allow you to exit a scope. Within an `if` statement or loop,
it exits the scope prematurely. Within the bottom scope, it is necessary
in order to exit the program gracefully. Not using a safeword in a
program is undefined behavior/implementation dependent.

    DECLARE SAFEWORD <safeword>
    ...
    [<safeword>]
