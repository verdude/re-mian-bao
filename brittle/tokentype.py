from enum import Enum

class TokenType(Enum):
    # other
    eof = 0

    # literals
    ident = 1
    string = 2
    number = 3

    # single char
    questionmark = 4
    bang = 5
    leftparen = 6
    rightparen = 7
    dot = 8
    dash = 9

    # multi char
    arrow = 10

    # keywords
    true = 11
    false = 12
