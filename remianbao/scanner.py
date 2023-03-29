from remianbao.token import Token
from remianbao.tokentype import TokenType


class Scanner:
    def __init__(self, filename: str):
        self.filename = filename
        self.tokens = []
        self.file = open(filename, "r")

    def scan(self):
        while self.get_token():
            self.tokens.append(self.curr_token)

    def get_token(self):
        c = self.file.read(1)

        if c == "?":
            tt = TokenType.questionmark
        elif c == "!":
            tt = TokenType.bang
        elif c == "(":
            tt = TokenType.leftparen
        elif c == ")":
            tt = TokenType.rightparen
        elif c == ".":
            tt = TokenType.dot
        elif c == "-":
            tt = TokenType.dash
        elif c.islower():
            tt = TokenType.bang
        elif c == "!": # upper
            tt = TokenType.bang
        else:
            print("invalid char", c)
            return
