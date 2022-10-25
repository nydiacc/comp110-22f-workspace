"""EX02 - One shot wordle."""

__author__ = "730563759"

secret: str = "python"
guess: str = input("What is your 6-letter guess? ")
thread: str = ""
character: int = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


if len(guess) != len(secret):
    while len(guess) != len(secret):
        # looping through attempts for mistakes about guess length.
        guess = input("That was not 6 letters! Try again: ")

while character < len(secret):
    # this while loop evaluates each index to assign the colored square.
    if guess[character] == secret[character]:
        thread += GREEN_BOX
    else:
        character_loop: int = 0
        present: bool = False
        while character_loop < len(secret):
            # this loops the entire secret to find a matching index for guess
            if guess[character] == secret[character_loop]:
                present = True
            character_loop += 1
        if present:
            thread += YELLOW_BOX
        else:
            thread += WHITE_BOX
    character += 1

print(thread)
if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon")
