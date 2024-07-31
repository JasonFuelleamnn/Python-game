from dataclasses import dataclass

@dataclass
class Item:
    name: str
    durability: int

    def __hash__(self) -> int:
        return hash(self.name)


