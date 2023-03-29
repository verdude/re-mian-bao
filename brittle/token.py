from typing import Any
from brittle.tokentype import TokenType


class Token:
    def __init__(self, *, tt: TokenType, literal: Any):
        self._type = tt
        self._literal = literal
