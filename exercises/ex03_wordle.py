"""EX03 - Structured Wordle."""

__author__ = "730563759"


def contains_char(char_loop: str, char_present: str) -> bool:
    """This function loops through the string to determine if the character is present."""
    assert len(char_present) == 1. 
    i: int = 0
    while len(char_loop) > i:
        # loop to check if word contains character
        if char_loop[i] == char_present:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of boxes if characters' indices match."""
    assert len(guess) == len(secret)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    thread: str = ""
    i: int = 0
    while len(secret) > i:
        # Runs through the whole word using previous function
        if contains_char(secret, guess[i]):
            if guess[i] == secret[i]:
                thread += green_box
            else:
                thread += yellow_box
        else:
            thread += white_box
        i += 1
    return thread 


def input_guess(char_guess: int) -> str:
    """Given the char_guess length, ensure the length of the inputed guess matches."""
    guess: str = str(input(f"Enter a {char_guess} character word: "))
    if len(guess) != int(char_guess):
        while len(guess) != int(char_guess):
            # Loop until there are the correct amount of characters
            guess = str(input(f"That wasn't {char_guess} chars! Try again: "))
    if len(guess) == int(char_guess):
        return guess
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    guess: str = ""
    secret: str = "codes"
    turn: int = 1
    while int(turn) <= 6:
        # Loop through the whole wordle turns
        print(f"=== Turn {turn}/6 ===")
        guess = (input_guess(len(secret)))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return
        else:
            turn += 1
    print("X/6 - Sorry try again tomorrow!")
    return
    