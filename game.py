import time
clear = "\x1b" + "[2J" + "\x1b" + "[H"

title = "The HIGH SCORE Game"
welcome = "Try and beat the high score!"

# Game loop
high_score = 0
while True:
    print(clear)
    time.sleep(0.1)
    print(title)
    print(f"High Score: {high_score}")
    print()
    print(welcome)
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
        print(clear)
        time.sleep(0.1)
        print("OOPS! Score must be a whole number.")
        time.sleep(1.5)
        continue

    # Is input new high score?    
    if score > high_score:
        high_score = score

        for i in range(3):
            print(clear)
            time.sleep(0.1)
            print("NEW HIGH SCORE!!!")
            time.sleep(.4)

    else:
        print(clear)
        print("Better luck next time!")
        time.sleep(1.5)
    
    print()
    
print("Thanks for playing!")
