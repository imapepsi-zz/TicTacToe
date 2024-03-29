import GameFunctions
import ComputerAI

while True:
    diagramBoard = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    gameBoard = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}

    # Choose the Letters
    userLetter = GameFunctions.getUserLetter()
    compLetter = GameFunctions.getCompLetter(userLetter)

    # Who goes first
    userGoesFirst = GameFunctions.willUserBeFirst()

    # Draw the board with numbers to show the key
    GameFunctions.drawBoard(diagramBoard)
    print("This the Board Diagram")

    # Show Blank board
    GameFunctions.drawBoard(gameBoard)


    if userGoesFirst:
        while True:
            GameFunctions.userTurn(gameBoard, userLetter)
            GameFunctions.drawBoard(gameBoard)
            if GameFunctions.winnerMessage(gameBoard, userLetter, compLetter):
                break
            if GameFunctions.checkIfFull(gameBoard):
                print("Board is Full. Tie")
                break

            print("Computer's Turn")
            ComputerAI.compTurn(gameBoard, compLetter, userLetter, ComputerAI.findEmptySpaces(gameBoard))
            GameFunctions.drawBoard(gameBoard)
            if GameFunctions.winnerMessage(gameBoard, userLetter, compLetter):
                break
            if GameFunctions.checkIfFull(gameBoard):
                print("Board is Full. Tie")
                break

    else:
        while True:
            print("Computer's Turn")
            ComputerAI.compTurn(gameBoard, compLetter, userLetter, ComputerAI.findEmptySpaces(gameBoard))
            GameFunctions.drawBoard(gameBoard)
            if GameFunctions.winnerMessage(gameBoard, userLetter, compLetter):
                break
            if GameFunctions.checkIfFull(gameBoard):
                print("Board is Full. Tie")
                break

            GameFunctions.userTurn(gameBoard, userLetter)
            GameFunctions.drawBoard(gameBoard)
            if GameFunctions.winnerMessage(gameBoard, userLetter, compLetter):
                break
            if GameFunctions.checkIfFull(gameBoard):
                print("Board is Full. Tie")
                break

    again = input("Do you want to play again? y or n: ").lower()
    if again == "n":
        break;
    elif again == "y":
        continue
    else:
        print("I'm not sure I understand, Let's play again another time.")

# Ask user for square and mark
# Computer's turn
# Check for winner
# Continue loop


