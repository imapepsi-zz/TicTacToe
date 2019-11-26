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


def checkIfWin(board, letter, possibleMoves):
    """Look at all the empty spaces in the board and check if that space will allow the computer to win"""
    for move in possibleMoves:  # Look at each square of the board
        boardCopy = board.copy()
        if GameFunctions.checkMove(boardCopy, move):  # if the space is empty
            GameFunctions.markSquare(boardCopy, letter, move)  # Mark the space
            if GameFunctions.checkForWinner(boardCopy, letter):  # Check if winner
                return True, move  # If winner return that key and computer will go there

    return False, -1


# Comp turn
def compTurn(board, computerLetter, userLetter, possibleMoves):
    """If the computer can win mark that square, if the user can win block that square, if none pick random one"""
    canCompWin, square = checkIfWin(board, computerLetter, possibleMoves)

    if canCompWin is False:  # If the Computer can't win check if the user can win and block that spot
        canUserWin, square = checkIfWin(board, userLetter, possibleMoves)

        if canUserWin is False:  # If the User can't win either pick random spot
            square = random.choice(possibleMoves)

    GameFunctions.markSquare(board, computerLetter, square)





