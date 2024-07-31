def noZeroes(n: list) -> bool:
    for i in n: 
        if i == 0:
            return False
    return True
# a function that you give a list of numbers to, and it returns
# true 

# [] {} 

# evens: list[int] = []
def evenNumber(numbers: list[int]) -> list[int]:
    evens: list[int] = []
    for n in numbers: 
        if n % 2 == 0:
            evens.append(n)
    return evens
        
# return, dont print

# True, not true
# joyce: # function that takes in a list of words and tells you how many words are great than 3 characters
def overThreeChar(words: list[str]) -> int:
    longWords = 0
    for w in words: 
        if len(words) > 3:
            longWords += 1 
    return longWords

def wordscontaining(character: str, words: list[str]) -> list[str]:
    wordsWithIt: list[str] = []
    for w in words:
        if character in w:
            wordsWithIt.append(w)
    return wordsWithIt

wordscontaining('a', ['apple', 'banana', 'orange', 'grape', 'kiwi'])
wordscontaining('e', ['apple', 'banana', 'orange', 'grape', 'kiwi'])