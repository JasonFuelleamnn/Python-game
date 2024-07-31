from dataclasses import dataclass
from typing import Literal
from Item import Item

@dataclass
class Food(Item):
    expiration: float
    nutrition: int
    sanity_points: int

    def __hash__(self) -> int:
        return hash(self.name)

