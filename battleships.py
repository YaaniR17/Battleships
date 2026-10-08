import random

board = [[0]*10 for _ in range(10)]

def draw(hide=True):
    print("  0 1 2 3 4 5 6 7 8 9")
    for i, row in enumerate(board):
        line = str(i) + " "
        for cell in row:
            if cell == 0 or (cell == 1 and hide): line += "~ "
            elif cell == 1: line += "S "
            elif cell == 2: line += "O "
            else: line += "X "
        print(line)

ships_placed = 0
while ships_placed < 10:
    r, c = random.randint(0, 9), random.randint(0, 9)
    if board[r][c] == 0:
        board[r][c] = 1
        ships_placed += 1

turns = 35
hits = 0

print("Battleship! Sink 10 ships. (~ = water, O = miss, X = hit)")

while turns > 0 and hits < 10:
    print(f"\nTurns left: {turns}")
    draw()

    try:
        r = int(input("Row (0-9): "))
        c = int(input("Col (0-9): "))
    except:
        print("numbers only pls")
        continue

    if not (0 <= r <= 9 and 0 <= c <= 9):
        print("off the board, try again")
        continue

    if board[r][c] in [2, 3]:
        print("already guessed there")
        continue

    if board[r][c] == 1:
        print("HIT!")
        board[r][c] = 3
        hits += 1
    else:
        print("miss.")
        board[r][c] = 2
        
    turns -= 1

print("\nGame Over")
if hits == 10:
    print("you win!")
else:
    print("out of turns. you lose.")
    draw(hide=False)
