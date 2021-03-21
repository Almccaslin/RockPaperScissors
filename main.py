import random
x = random.randint(1, 3)

c = 0

player = input(str("Name: "))

p = open(player, "a")

rps = input("Rock, Paper, or Scissors?")

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
if (x == 2 and y == "PAPER"):
    c = 1
if (x == 3 and y == "SCISSORS"):
    c = 1

if (x == 1 and y == "PAPER"):
    c = 2
if (x == 1 and y == "SCISSORS"):
    c = 3

if (x == 2 and y == "SCISSORS"):
    c = 2
if (x == 2 and y == "ROCK"):
    c = 3

if (x == 3 and y == "ROCK"):
    c = 2
if (x == 3 and y == "PAPER"):
    c = 3

if (c == 1):
    print("It's a tie.")
    p.write("\nIt's a tie.\n")
elif (c == 2):
    print("You win.")
    p.write("\nYou win.\n")
elif (c == 3):
    print("You lose.")
    p.write("\nYou lose.\n")
else:
    print("Invalid Respose")
    p.write("\nInvalid respose\n")

p.close()
