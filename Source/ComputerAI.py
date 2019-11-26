import random
import GameFunctions

# Create Possible moves for computer
def findEmptySpaces(board):
    possibleMoves = []
    for key in board:
        if board[key] == "":
            possibleMoves.append(board[key])
        else:
            continue

    return possibleMoves

# Comp turn
def compTurn(board, letter, possibleMoves):
    while True:
        square = random.choice(possibleMoves)
        if square < 1 or square > 9:
            continue
        else:
            if checkMove(board, square):
                break
            else:
                continue  # If can't mark square keep asking for a square

    markSquare(board, letter, square)