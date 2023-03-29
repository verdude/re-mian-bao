from typing import Any, Optional
from remianbao.tokentype import TokenType


class Token:
    def __init__(self, *, tt: TokenType, literal: Optional[Any]):
        self._type = tt
        self._literal = literal

    def __repr__(self) -> str:
        return f"Token({self._type}, {self._literal})"
