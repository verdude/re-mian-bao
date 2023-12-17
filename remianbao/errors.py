from dataclasses import dataclass

@dataclass
class Messages:
    strerror = "Invalid string."
    tkerror = "Invalid token."


@dataclass
class Err:
    msg: str
    line: str
    offsets: set[int]
