import random


# Display board
def drawBoard(board):
    """Draw Game Board and Pass in a dictionary that represents the board"""
    print("{:^3}|{:^3}|{:^3}".format(board[1], board[2], board[3]))
    print("---+---+---")
    print("{:^3}|{:^3}|{:^3}".format(board[4], board[5], board[6]))
    print("---+---+---")
    print("{:^3}|{:^3}|{:^3}".format(board[7], board[8], board[9]))


# Get user and comp letter - X or O
def getUserLetter():
    """Ask the user what letter they would like to be"""
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
def checkMove(board, square):
    if board[square] != "":
        print("You can not go there, Please select another Square.")
        return False  # If can't mark square return False
    else:
        return True


# User turn
def userTurn(board, letter):
    while True:
        square = input("What square would you like to mark? (1 - 9): ")
        if square < 1 or square > 9:
            continue
        else:
            if checkMove(board, square):
                break
            else:
                continue # If can't mark square keep asking for a square

    markSquare(board, letter, square)

# Check if there's a winner
def checkWinner(b, l):
    """ Check if X or O has won, b = board and l = letter"""
    # Top, middle, bottom, diagonals (start from corner 1, then start from corner 3)
    return (b[1] == b[2] and b[1] == b[3] and b[1] == l) or \
           (b[4] == b[5] and b[4] == b[6] and b[4] == l) or \
           (b[7] == b[8] and b[7] == b[9] and b[7] == l) or \
           (b[1] == b[5] and b[1] == b[9] and b[1] == l) or \
           (b[3] == b[5] and b[3] == b[7] and b[3] == l)




