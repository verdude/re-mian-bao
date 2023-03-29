import re
from typing import Optional, Iterator
from remianbao.token import Token
from remianbao.tokentype import TokenType


class Scanner:
    def __init__(self, filename: str):
        self.filename = filename
        self.tokens = []
        self._file = open(filename, "r")
        self.error = False

        self.idre = r"[a-z][a-zA-Z0-9\-]*[a-z0-9]"
        self.strre = r'"(.*)"'
        self._lines = self._start_gen()

    def _start_gen(self) -> Iterator[str]:
        gen = (line for line in self._file.readlines())
        for line in gen:
            while len(line) > 0:
                tokenlength = yield line
                line = line[tokenlength:].lstrip()

    def scan(self):
        print("scanning")

        for line in self._lines:
            self.scantoken(line)

        print("done scanning")
        print("Errors:", self.error)
        self._file.close()
        return self.tokens

    def _savetk(self, tk: Token):
        try:
            self.tokens.append(tk)
            self._lines.send(len(tk))
        except StopIteration:
            print("should stop")


    def scantoken(self, line: str):
        c = line[0]
        if c == "?":
            self._savetk(Token(tt=TokenType.questionmark, literal=c))
        elif c == "!":
            self._sendtk(Token(tt=TokenType.bang, literal=c))
        elif c == "(":
            self._savetk(Token(tt=TokenType.leftparen, literal=c))
        elif c == ")":
            self._savetk(Token(tt=TokenType.rightparen, literal=c))
        elif c == ".":
            self._savetk(Token(tt=TokenType.dot, literal=c))
        elif c == '"':
            match = re.search(f"^{self.strre}", line)
            if not match:
                self.error = True
                return
            literal = match.group(0)
            value = match.group(1)
            self._savetk(Token(tt=TokenType.string, literal=literal, value=value))
        elif c == "-":
            if line[1] != ">":
                self.error = True
                return
            self._savetk(Token(tt=TokenType.dash, literal="->"))
        elif c.islower():
            match = re.search(f"^{self.idre}", line)
            if not match:
                self.error = True
                return
            literal = match.group(0)
            self._savetk(Token(tt=TokenType.ident, literal=literal))
        elif c.isupper():
            # TODO: variables re
            match = re.search(f"^{self.idre}", line)
            if not match:
                self.error = True
                return
            literal = match.group(0)
            self._savetk(Token(tt=TokenType.variable, literal=literal))
        else:
            print("invalid char", c)
            self._savetk(Token(tt=TokenType.invalid, literal=c))
            self.error = True
