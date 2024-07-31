from __future__ import annotations
from dataclasses import dataclass
from typing import Literal
from Item import Item
# from Room import Room
import Room

@dataclass
class Person:
    name: str
    age: int
    weight: float
    height: int
    gender: Literal['Male'] | Literal['Female']
    health: int
    stamina: int
    satiation: int
    intelligence: int
    sanity: int 
    inventory: set[Item]
    room: Room.Room

    # set = like a list, but the same object cannot be added twice
    # NOTE: the same TYPE of object can be added twice. like two swords
    # but the literal same sword cannot be added twice.
    # like, if there is a sword on the ground...
    # can you put it in your inventory twice? no. 
    # you can have 5 different golden coins in a set,
    # but you can't have the same 1 golden coin added 5 times.
    # a list allows both. A list would allow duplicating the same coin.
    


    #list = a bag of stuff. 
    def __hash__(self) -> int:
        return hash(self.name)