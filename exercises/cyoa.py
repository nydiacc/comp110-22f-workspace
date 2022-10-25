"""Choose Your Own Adventure - Hide and Seek."""
from random import randint
__author__ = "730563759"

points: int = 0
comp_points = 0
player: str = ""
round_i: int = 0
again_i: int = 0
RED_CIRCLE: str = "\U0001F534"
YELLOW_CIRCLE: str = "\U0001F7E1"
GREEN_CIRCLE: str = "\U0001F7E2"


def greet() -> None:
    """Greets player to begin game."""
    global player
    player = input("What is your name? ")
    print(f"Hey, {player}! Let's play a game of hide and seek. \nWhoever hides best or seeks best that round, gets 25 points. \nThe first person to 100 points wins!")
    return None


def start_game() -> str:
    """This is the first round that begins the game."""
    global points, round_i
    question: str = input("Let's play a quick match of heads or tails. \nHeads or Tails to see who gets to hide first, or type quit to exit the game.\nType heads or tails to choose: ")
    heads_tails: int = randint(0, 1)
    response: str = ""
    return_option: str = ""

    if heads_tails == 0:
        response = "heads"
    elif heads_tails == 1:
        response = "tails"

    if question == response:
        return_option = "player_hide"
        print("Congrats! You get to hide first")
    elif question == "quit":
        round_i += 1
        print(f"=== GAME OVER ===  {player}'s points: {points} === Computer's points: {comp_points} ===\n{player}, you quit on Round {round_i}")
        quit()

    elif question != response: 
        return_option = "comp_hide"
        print("You chose wrong, I get to hide first!")
    return return_option

    
def comp_hide() -> int:
    """This is the computer picking a hiding spot."""
    hidden_guess: int = randint(0, 2)
    return hidden_guess


def comp_seek() -> int:
    """This is the computer guessing where the player hid."""
    seek_guess: int = randint(0, 2)
    return seek_guess


def player_hide() -> int:
    """This is where the player gets to choose where to hide."""
    player_choice: str = input(f"{player}, it's your turn to hide, choose which circle you want to hide behind\n{RED_CIRCLE}  {YELLOW_CIRCLE}  {GREEN_CIRCLE} \nType the color you want to hid behind: ")
    player_guess: int = 0
    counter: int = 0

    if player_choice == "red":
        player_guess = 0
        counter += 1
    elif player_choice == "yellow":
        player_guess = 1
        counter += 1
    elif player_choice == "green":
        player_guess = 2
        counter += 1
    elif player_choice == "quit":
        print(f"=== GAME OVER ===  {player}'s points: {points} === Computer's points: {comp_points} ===\n{player}, you quit on Round {round_i}")
        quit()
    
    while counter < 1:

        player_choice = str(input("You must have spelled something wrong! Please type red, yellow, or green: "))
        if player_choice == "red":
            player_guess = 0
            counter += 1
        elif player_choice == "yellow":
            player_guess = 1
            counter += 1
        elif player_choice == "green":
            player_guess = 2
            counter += 1
        elif player_choice == "quit":
            print(f"=== GAME OVER ===  {player}'s points: {points} === Computer's points: {comp_points} ===\n{player}, you quit on Round {round_i}")
            quit()

    return player_guess


def player_seek() -> int:
    """The player is guessing where the computer is hiding."""
    player_choice: str = input(f"Guess where I'm hiding!\n{RED_CIRCLE}  {YELLOW_CIRCLE}  {GREEN_CIRCLE} \nChoose between red, yellow, or green: ")
    player_guess: int = 0
    i: int = 0

    if player_choice == "red":
        player_guess = 0
        i += 1
    elif player_choice == "yellow":
        player_guess = 1
        i += 1
    elif player_choice == "green":
        player_guess = 2
        i += 1
    elif player_choice == "quit":
        print(f"=== GAME OVER ===  {player}'s points: {points} === Computer's points: {comp_points} ===\n{player}, you quit on Round {round_i}")
        quit()
    
    while i < 1:
        player_choice = str(input("You must have spelled something wrong! Please type red, yellow, or green: "))
        if player_choice == "red":
            player_guess = 0
            i += 1
        elif player_choice == "yellow":
            player_guess = 1
            i += 1
        elif player_choice == "green":
            player_guess = 2
            i += 1
        elif player_choice == "quit":
            print(f"=== GAME OVER ===  {player}'s points: {points} === Computer's points: {comp_points} ===\n{player}, you quit on Round {round_i}")
            quit()

    return player_guess


def player_guess_correct(player_guess: int, comp_guess) -> str:
    """Give points to player if the guess is correct."""
    global points, comp_points
    return_comp_hide: str = "comp_hide"
    return_player_hide: str = "player_hide"
    if player_guess == comp_guess:
        print("Congrats! You guessed the right spot.")
        points += 25
        return return_player_hide
    else:
        print("Oops, you guessed wrong")
        comp_points += 25
        return return_comp_hide


def comp_guess_correct(comp_guess: int, player_guess: int) -> str:
    """Gives points to computer if the guess is correct."""
    global points, comp_points
    return_comp_hide: str = "comp_hide"
    return_player_hide: str = "player_hide"
    if comp_guess == player_guess:
        print("I guessed your spot, I win!")
        comp_points += 25
        return return_comp_hide
    else:
        print("Great hiding spot, I didn't find you.")
        points += 25
        return return_player_hide


def rounds() -> str:
    """Declares which round it's on."""
    global round_i, player, points, comp_points
    round_i += 1
    current_round: str = f"=== Round {round_i} === {player}'s points: {points} === Computer's points: {comp_points} ==="
    return current_round


def main() -> None:
    """This is the beginning of the game."""
    global player, points, comp_points, round_i, again_i
    points = 0
    comp_points = 0
    difference: int = 0
    decision: str = ""
    greet()
    game_mode: str = start_game()

    while again_i < 1:
        while points < 100 and comp_points < 100:

            if game_mode == "player_hide":
                print(rounds()) 
                if comp_guess_correct(player_hide(), comp_seek()) == "comp_hide":
                    game_mode = "comp_hide"
                else:
                    game_mode = "player_hide"

            elif game_mode == "comp_hide":
                print(rounds())
                if player_guess_correct(comp_hide(), player_seek()) == "player_hide":
                    game_mode = "player_hide"
                else:
                    game_mode = "comp_hide"
            
        if points == 100:
            difference = points - comp_points
            print(f"=== GAME OVER ===  {player}'s points: {points} === Computer's points: {comp_points} ===\nCongrats, {player}! You won on Round {round_i} and beat me by {difference} points")
        elif comp_points == 100:
            difference = comp_points - points
            print(f"=== GAME OVER ===  {player}'s points: {points} === Computer's points: {comp_points} ===\n{player}, you lost on Round {round_i} by {difference} points!")

        decision = str(input("Do you want to play again? yes or no?: "))
        if decision == "yes":
            print("Awesome! Let's play another round!")
            points = 0
            comp_points = 0
            round_i = 0
            again_i = 0
        if decision == "no":
            print("Okay bye!")
            again_i += 1

    return None


if __name__ == "__main__":
    main()