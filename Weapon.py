from Item import Item

from dataclasses import dataclass

@dataclass
class Weapon(Item):
    damage: int
    
    def __hash__(self) -> int:
        return hash(self.name)