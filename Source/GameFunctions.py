import random

# Display board
def drawBoard(board):
    """Draw Game Board and Pass in a dictionary that represents the board"""
    print("{:^3}|{:^3}|{:^3}".format(board[0], board[1], board[2]))
    print("---+---+---")
    print("{:^3}|{:^3}|{:^3}".format(board[3], board[4], board[5]))
    print("---+---+---")
    print("{:^3}|{:^3}|{:^3}".format(board[6], board[7], board[8]))

# Get user and comp letter - X or O
def getUserLetter():
    while True:
        letter = input("What letter would you like to play as? X or O: ").upper()
        if letter != "X" and letter != "O":
            continue
        else:
            return letter

def getCompLetter(user):
    if user == "X":
        return "O"
    elif user == "O":
        return "X"

# Who will go first
def willUserBeFirst():
    randNum = random.randint(0, 1)
    if randNum == 0:
        return True
    else:
        return False

# Mark a square with letter
def markSquare(board, letter, square):
    """Pass in board, letter, square to mark and reassign that square"""
    board[square] = letter

# Check that the square is not already marked
def checkMove(board, move):
    if board[move] != "":
        print("You can not go there, Please select another Square.")

# User turn
def userTurn():
    input("What square would you like to mark? (1 - 9): ")

# Comp turn


#
