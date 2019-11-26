import random
import GameFunctions


# Create Possible moves for computer
def findEmptySpaces(board):
    possibleMoves = []
    for key in board:
        if GameFunctions.checkMove(board, key):
            possibleMoves.append(key)
        else:
            continue
    return possibleMoves

def randomChoiceFromList(board, moveList):
    """Check if the desired moves from moveList are valid"""
    validMoves = []
    for move in moveList:
        if GameFunctions.checkMove(board, move):
            validMoves.append(move)

    if len(validMoves) != 0:
        return random.choice(validMoves)
    else:
        return None;

def checkIfWin(board, letter, possibleMoves):
    """Look at all the empty spaces in the board and check if that space will allow the computer to win"""
    for move in possibleMoves:  # Look at each square of the board
        boardCopy = board.copy()
        if GameFunctions.checkMove(boardCopy, move):  # if the space is empty
            GameFunctions.markSquare(boardCopy, letter, move)  # Mark the space
            if GameFunctions.checkForWinner(boardCopy, letter):  # Check if winner
                return True, move  # If winner return that key and computer will go there

    return False, -1

def checkCornersCenterSides(board):
    """Check if corners, center, side are empty (if that order)"""
    move = randomChoiceFromList(board, [1, 3, 7, 9])
    if move is not None:
        return move

    if GameFunctions.checkMove(board, 5):
        return 5

    move = randomChoiceFromList(board, [2, 4, 6, 8])
    if move is not None:
        return move


# Comp turn
def compTurn(board, computerLetter, userLetter, possibleMoves):
    """If the computer can win mark that square, if the user can win block that square, if none check empty"""
    canCompWin, square = checkIfWin(board, computerLetter, possibleMoves)

    if canCompWin is False:  # If the Computer can't win check if the user can win and block that spot
        canUserWin, square = checkIfWin(board, userLetter, possibleMoves)

        if canUserWin is False:  # If the User can't win either pick random spot
            square = checkCornersCenterSides(board)

    GameFunctions.markSquare(board, computerLetter, square)





