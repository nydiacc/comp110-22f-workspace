"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730563759"

word: str = str(input("Enter a 5-character word: "))
counter: int = 0
if 5 == len(word):
    character: str = str(input("Enter a single character: "))
    if 1 == len(character):
        print("Searching for " + character + " in " + word)
        if character == word[0]:
            print(character + " found at index 0")
            counter = counter + 1
        if character == word[1]:
            print(character + " found at index 1")
            counter = counter + 1
        if character == word[2]:
            print(character + " found at index 2")
            counter = counter + 1
        if character == word[3]:
            print(character + " found at index 3")
            counter = counter + 1
        if character == word[4]:
            print(character + " found at index 4")
            counter = counter + 1 
    else:
        print("Error: Word must contain 5 characters")
        quit()
else:
    print("Error: Word must contain 5 characters")
    quit()

if counter == 1: 
    print(str(counter) + " instance of " + character + " found in " + word)
if counter > 1: 
    print(str(counter) + " instances of " + character + " found in " + word)
else:
    print("No instances of " + character + " found in " + word)