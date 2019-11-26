import GameFunctions

gameBoard = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}


userLetter = GameFunctions.getUserLetter()
compLetter = GameFunctions.getCompLetter(userLetter)

userGoesFirst = GameFunctions.willUserBeFirst()

GameFunctions.drawBoard(gameBoard)

