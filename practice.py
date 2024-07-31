# NOTE: the same TYPE of object can be added twice. like two swords
    # but the literal same sword cannot be added twice.
    # like, if there is a sword on the ground...
    # can you put it in your inventory twice? no. 
    # you can have 5 different golden coins in a set,
    # but you can't have the same 1 golden coin added 5 times.
    # a list allows both. A list would allow duplicating the same coin.

    #list = a bag of stuff. 


def multiplybytwo(n: int) -> int:
    return n *2
    
    

def negative(n: int) -> int:
    return n * -1

def repeatThree(n: str) -> str:
    return n * 3

def multiplyThree(a: int, b: int, c: int ) -> int:
    return a * b * c

def subtract(a: int, b: int) -> int:
    return a - b
    
def howmany(words: list[str]) -> str:
    count = 0
    for x in words:
        count += 1
    return count

def biggestNumber(numbers: list[int]) -> int:
    knownbiggest = numbers[0]
    for x in numbers:
        if x > knownbiggest:
            knownbiggest = x
    return knownbiggest
        
def smallestNumber(numbers: list[int]) -> int:
    knownsmallest = numbers[0]
    for x in numbers:
        if x < knownsmallest:
            knownsmallest = x
    return knownsmallest

[5,37,1,39,1,39,34,5,9,1,53,1,384,194,3679,3,104]


# print(howmany(['hello','goodbye','yes']))  # 3   


# subtract(5, 3)
# subtract(3, 5)
# [] () {} <>

# multiplyThree(5,2,3) == 30 

# functino that takes in a list of words and tells you how many words are in the liston. this one is probably hardest

# function that takes in a list of numbers and tells you what the biggest number is


# function that takes in a list of numbers and tells you what the smallest number is


# joyce:
# function that takes in a list of words and tells you how many words are great than 3 characters