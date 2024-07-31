from dataclasses import dataclass
from typing import Literal

from Room import Room
from Item import Item
from Food import Food
from Person import Person
from Weapon import Weapon


def choose_name() -> str:
    name = input("Enter your name: ")
    if len(name) == 0:
        print("Name must be at least 1 character long")
        return choose_name()
    return name

def choose_age() -> int:
    age = int(input("Enter your age: "))
    if age < 13:
        print("Sorry you are too young :(")
        quit()
    return age

def choose_gender() -> str:
    gender = input("Please enter your gender? Male or Female?")
    if gender not in ["Male", "Female"]:
        print("Please enter a Male or Female")
        return choose_gender()
    return gender

def create_items() -> list[Item]:
    weapons = [
        Weapon("Knife", 120, 20),
        Weapon("Bow", 70, 15),
    ]
    foods = [
        Food("Bread", 1, 5, 6, 20),
        Food("Apple", 1, 3, 5, 10),
        Food("Steak", 1, 7, 8, 40),
        Food("Baked potato", 1, 10, 6, 30),
        Food("Rotten tomato", 1, 0, 1, -40),
    ]
    miscellaneous = [
        Item("Stick", 1),
        Item("Rock", 1),
        Item("Dirt", 1),
        Item("Coin", 1)
    ]
    return weapons + foods + miscellaneous

def create_room1() -> Room:
    room = Room("Bedroom", 60, set(), set(), set())
    room.items.add(Item("Coin", 1))
    room.people.add(
        Person("Bob", 20, 50, 5, 'Male', 100, 10, 100, 100, 100, set(), room))
    return room

def create_room2() -> Room:
    room = Room("Kitchen", 40, set(), set(), set()) 
    
    room.items.add(Weapon("Knife", 120, 20))
    room.items.add(Food("Bread", 1, 5, 6, 20))
    room.items.add(Food("Apple", 1, 3, 5, 10))
    room.items.add(Food("Steak", 1, 7, 8, 40))
    room.items.add(Food("Baked potato", 1, 10, 6, 30))
    room.items.add(Food("tomato", 1, 0, 1, -40))

    return room

def create_rooms(player: Person) -> list[Room]:
    room1 = create_room1()
    room2 = create_room2()
    room1.destinations.add(room2)
    room2.destinations.add(room1)
    room1.people.add(player)

    return [room1, room2]
    


# return gender
def main() -> None:
    name = choose_name()
    print(f"Hello {name}")

    age = choose_age()
    print("Great, you are old enough to play the game.")

    gender = choose_gender()

    player = Person(name, age, 50, 180, gender, 100, 100, 100,100, 100, set(), None)

    rooms = create_rooms(player)
    
    
    print("Welcome to our game. Type help to see commands")

    # we now need to organize all of this stuff, into their own functions
    running = True
    while running == True:
        command = input("please enter your command: ")
        if command == "quit":
            print("Goodbye")
            running = False
        if command == "help":
            print("Commands:")
            print("eat: eat the food in your inventory")
            print("quit - to quit the game") #done
            print("pickup - pick up an item close to you") #done
            print("drop - drop an item from your inventory") #done
            print("attack: to attack an animal or another human")
            print("move: to move to a new room/location")
            print("inspect: to look at an object and gain a description of what it does") 
            print("inv: to look at what is in your inventory") 
           
        if command == "pickup":
            print("Which item?")
            if len(player.room.items) == 0:
                print("sorry there are no items in this room to pickup")
            else:
                for item in player.room.items:
                    print(item.name)
                choice = input("enter the item name:")
                for item in player.room.items:
                    if item.name == choice:
                        player.inventory.add(item)
                        player.room.items.remove(item)
                        print(f"You picked up {item.name}")  
                        break
        
        if command == "drop":
            print("Which item would you like to drop? ")
            for item in player.inventory:
                print(item.name)
            choice = input("Enter the Item name: ")
            for item in player.inventory:
                if item.name == choice:
                    player.inventory.remove(item)
                    player.room.items.add(item)
                    print(f"You dropped {item.name}")
                    break


        if command == "inv":
            print("These items are in your inventory: ")
            for item in player.inventory:
                print(item.name)
        
        if command == "eat":
            print("Which item?")
            
        if command == "move":
            print("Which room?")
            for room in player.room.destinations:
                print(room.name)
            choice = input("Enter the room name: ")
            for room in player.room.destinations:
                if room.name == choice:
                    player.room = room
                    print(f"You are now in the {room.name}")
                    break
            
            



main()

