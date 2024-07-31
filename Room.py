from __future__ import annotations
from dataclasses import dataclass
from Person import Person
from Item import Item

@dataclass
class Room:
    name: str
    size: int
    people: set[Person]
    items: set[Item]
    destinations: set[Room]

    def __hash__(self) -> int:
        return hash(self.name)
    