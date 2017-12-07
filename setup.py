

class GameState(object):
    def __init__(self, board, turn, gameWin, isFull):
        self.board = board
        self.turn = turn
        self.gameWin = gameWin
        self.isFull = isFull
    
    def printBoard(self, rows: int, cols: int):
        '''
        Prints the current board
        '''
        
        for item in range(rows):
            myUI = ''
            for puck in range(cols):
                if self.board[item][puck] == 0:
                    myUI += '. '
                if self.board[item][puck] == 1:
                    myUI += 'B '
                if self.board[item][puck] == 2:
                    myUI += 'W '
            print(myUI)
        print('Turn: {}'.format(self.turn))
        return

    def numColor(self, rows: int, cols: int, color: int):
        '''
        Takes a 1 or 2 and counts how many there
           are on the current board
        '''
        i = 0
        for item in range(rows):
            for puck in range(cols):
                if self.board[item][puck] == color:
                    i += 1
        return i

    def checkFull(self, rows: int, cols, int):
        '''
        Checks if the current board is full or not
        '''
        i = 0
        for item in range(rows):
            for puck in range(cols):
                if self.board[item][puck] == 0:
                    i += 1
        if i == 0:
            self.isFull = True
                    

def createBoard(rows: int, cols: int):
    '''
    Creates a two-dimensional list of just 0s
    '''
    
    board = []
    
    for num in range(rows):
        board.append([])
        for col in range(cols):
            board[-1].append(0)
    return board
        
def startGame(rows: int, cols: int, turn: str, align: str, gameWin: str) -> None:
    '''
    Starts the whole game with printed interface
    '''
    middleR = int((rows/2) - 1)
    middleC = int((cols/2) - 1)
    
    board = createBoard(rows, cols)
    isFull = False
    myGame = GameState(board, turn, gameWin, isFull)
    if align == 'B':
        myGame.board[middleR][middleC] = 1
        myGame.board[middleR][middleC + 1] = 2
        myGame.board[middleR + 1][middleC] = 2
        myGame.board[middleR + 1][middleC + 1] = 1
    else:
        myGame.board[middleR][middleC] = 2
        myGame.board[middleR][middleC + 1] = 1
        myGame.board[middleR + 1][middleC] = 1
        myGame.board[middleR + 1][middleC + 1] = 2
    
    return myGame
    

def theMeat(myGame: 'GameState', rows: int, cols: int):
    
    while myGame.isFull == False:
        try:
            print('B: {}  W: {}'.format(myGame.numColor(rows, cols, 1),
                                        myGame.numColor(rows, cols, 2)))
            myGame.printBoard(rows, cols)
            myGame.isFull = True
        except:
            print('YA DUN GOOFED')

if __name__== '__main__':
    rows = int(input())
    cols = int(input())
    turn = input()
    align = input()
    gameWin = input()
    
    game = startGame(rows, cols, turn, align, gameWin)
    theMeat(game, rows, cols)
























