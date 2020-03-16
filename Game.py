from GUI import showBoard, getInput, express

def board():
    x, y = getInput("Size of board?")
    board = [ [ " " for i in range(x) ] for j in range(y) ]
    return board


def modifyBoard(board, player):
    pointTaken = True
    while pointTaken:   
        x, y = getInput("Where to place dot")
        try:
            #Look if the point is already occupied
            if board[x-1][y-1] is ' ':
                pointTaken = False
            else:
                express("fuck off it's occupied")
        
        #If input is outside of board
        except IndexError as e:
            express("Outside of board!")
    
    board[x-1][y-1] = player
    return board


def startGame(board, player1, player2):
    currPlayer = player1
    turn = 1
    for i in range(len(board)*len(board[0])):
        showBoard(board)    
        #checkThePoint(board, x, y)
        
        board = modifyBoard(board, currPlayer)

        currPlayer = player1 if currPlayer == player2 else player2
    
    showBoard(board) 
    express("Game Over")

