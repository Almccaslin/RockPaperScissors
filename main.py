import random

c = 0
y = "a"

player = input(str("Name: "))
p = open(player, "a")


while (y != "STOP"):
    c = 0
    p = open(player, "a")
    rps = input("Rock, Paper, Scissors: ")
    x = random.randint(1, 3)
    if (x == 1):
        print("Computer: ROCK")
    if (x == 2):
        print("Computer: PAPER")
    if (x == 3):
        print("Computer: SCISSORS")

    y = rps.upper()
    print("Human: " + y)

    if (x == 1 and y == "ROCK"):
        c = 1
    if (x == 1 and y == "PAPER"):
        c = 2
    if (x == 1 and y == "SCISSORS"):
        c = 3

    if (x == 2 and y == "PAPER"):
        c = 1
    if (x == 2 and y == "SCISSORS"):
        c = 2
    if (x == 2 and y == "ROCK"):
        c = 3

    if (x == 3 and y == "SCISSORS"):
        c = 1
    if (x == 3 and y == "ROCK"):
        c = 2
    if (x == 3 and y == "PAPER"):
        c = 3

    if (c == 1):
        w = ("It's a tie.")

    elif (c == 2):
        w = ("You win.")

    elif (c == 3):
        w = ("You lose.")

    else:
        w = ("Invalid Response")

    print(w)
    y = (input("STOP to end: "))

    p.write(w)
    p.write("\n")

p.close()
