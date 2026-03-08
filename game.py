"""
=== THE HIGH SCORE GAME ===
Try and beat the high score!
"""
import time

title = "The High Score Game"
welcome = "Try and beat the high score!"
high_score = 0

def clear_screen():
    print("\x1b" + "[2J" + "\x1b" + "[H")

# Game loop
while True:
    clear_screen()
    time.sleep(0.1)
    print(f"=== {title.upper()} ===")
    print(welcome)
    print(f"High Score: {high_score}")
    print()
    # Get player input
    print("Enter your score:")
    player_input = input("> ")

    # Q = Quit
    if player_input.upper() == "Q":
        break

    # Is input a number?
    try:
        score = int(player_input)
    except ValueError:
        clear_screen()
        time.sleep(0.1)
        print("OOPS! Score must be a whole number.")
        time.sleep(1.5)
        continue

    # Is input new high score?    
    if score > high_score:
        high_score = score

        for i in range(3):
            clear_screen()
            time.sleep(0.1)
            print("NEW HIGH SCORE!!!")
            time.sleep(.4)

    else:
        clear_screen()
        print("Better luck next time!")
        time.sleep(1.5)
        clear_screen()
        time.sleep(.5)
        print("GAME OVER")
        time.sleep(2)
    print()
    
print("Thanks for playing!")
