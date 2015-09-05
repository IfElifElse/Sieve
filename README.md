# Sieve
Sieve is a BF extension that allows for shorter BF programs.

BF (shortened from Brainfuck) is an esoteric language with only 8 commands: > < + - . , [ ]

BF works with an infinite line of units called a tape. Each unit is set to 0 initially. With > and <, we can select
different units of tape. > selects the unit to the right of the currently selected one and < selects the unit to
the left. With + and -, we can increment and decrement the value in the current unit by one. , takes input and
stores its ASCII value in the selected unit. . prints the character within the selected unit to STDOUT. Brackets
([]) open and close loops, which will execute whatever's inside of them until the selected tape is 0.

There are a few commands that Sieve has that BF doesn't.

*:*
A colon writes the literal number in the selected tape unit to STDOUT.

    ++++:
would output `4`.

*;*
A semicolon takes integer input and stores it within the selected tape unit.

    ;++:
with the input `65` would output `67`.

*|*
A vertical bar is a sieve. A sieve executes the previous command until the number in the tape unit is equal to the number within the sieve.

    +|65|.
would output H, who's ascii value is 65.
