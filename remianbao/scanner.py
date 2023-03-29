from typing import Optional
from remianbao.token import Token
from remianbao.tokentype import TokenType


class Scanner:
    def __init__(self, filename: str):
        self.filename = filename
        self.tokens = []
        self.file = open(filename, "r")

        self.idre = r"[a-z][a-zA-Z0-9\-]*[a-z0-9]"

    def scan(self):
        print("scanning")
        while self.get_token():
            print(self.curr_token)
            self.tokens.append(self.curr_token)
        print("done scanning")
        return self.tokens

    def get_identifier(self) -> Optional[str]:



    def get_token(self) -> bool:
        c = self.file.read(1)

        if c == "?":
            self.curr_token = Token(tt=TokenType.questionmark, literal=c)
        elif c == "!":
            self.curr_token = Token(tt=TokenType.bang, literal=c)
        elif c == "(":
            self.curr_token = Token(tt=TokenType.leftparen, literal=c)
        elif c == ")":
            self.curr_token = Token(tt=TokenType.rightparen, literal=c)
        elif c == ".":
            self.curr_token = Token(tt=TokenType.dot, literal=c)
        elif c == "-":
            self.curr_token = Token(tt=TokenType.dash, literal=c)
        elif c.islower():
            self.curr_token = Token(tt=TokenType.bang, literal=c)
        elif c == "!": # upper
            self.curr_token = Token(tt=TokenType.bang, literal=c)
        else:
            print("invalid char", c)
            self.curr_token = None

        return self.curr_token is not None
