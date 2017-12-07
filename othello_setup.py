# Jackson Greaves jdgreave

import othello_inputs

class GameState(object):
    def __init__(self, board, turn, gameWin, isFull, isOver):
        self.board = board
        self.turn = turn
        self.gameWin = gameWin
        self.isFull = isFull
        self.isOver = isOver

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
            
    def isEmpty(self, row: int, col: int):
        '''
        Returns a boolean based on whether or not
           there is a puck in a specified position
        '''
        if self.board[row][col] == 0:
            return True
        else:
            return False
        
    def opponentColor(self, theTurn: int):
        '''
        Returns the numeric value for the opponent's
           turn; 
        '''
        opponentTurn = 0
        if theTurn == 1:
            opponentTurn = 2
        elif theTurn == 2:
            opponentTurn = 1
        return opponentTurn

    def noMoves(self) -> bool:
        if self.areMoves() == False:
            return True
        return False

    def endGame(self) -> bool:
        if self.noMoves():
            if self.areMoves() == False:
                return True
        return False

    def turnToInt(self):
        if self.turn == 'B':
            return 1
        if self.turn == 'W':
            return 2

    def turnToString(self):
        if self.turn == 'B':
            return 'Black'
        if self.turn == 'W':
            return 'White'

    def changePucks(self, move: ['moveHere']):        
        for option in move:
            
            for point in option.pucksToFlip:
                self.board[point[0]][point[1]] = self.turnToInt()
    
    def switchPlayer(self):
        '''
        Changes the GameState's turn to the
           opponent's turn
        '''
        if self.turn == 'B':
            self.turn = 'W'
        else:
            self.turn = 'B'

    def checkBoardMove(self, place: [int, int]):
        theTurn = self.turnToInt()
        moves = othello_inputs.moveCheck(self, theTurn)
        for move in moves:
            if move.point == place:
                return True
        return False

    def compileFlips(self, moves: ['moveHere'], RandC: [int, int]):
        flips = othello_inputs.makeTheMove(self, moves, RandC)
        return flips

    def makeFlips(self, move: ['moveHere']):
        theTurn = self.turnToInt()
        for option in move:
            self.board[option.point[0]][option.point[1]] = theTurn
            for point in option.pucksToFlip:
                self.board[point[0]][point[1]] = theTurn
                
    def getMoveCheck(self):
        return othello_inputs.moveCheck(self, othello_inputs.turnToNum(self.turn))

    def areMoves(self):
        return len(self.getMoveCheck()) > 0

    def whoWon(self):
        val = greaterScore(self)
        if self.gameWin == '>':
            if val == 1:
                return 'Black'
            if val == 2:
                return 'White'
            if val == 0:
                return 'Neither (you tied)'
        if self.gameWin == '<':
            if val == 1:
                return 'White'
            if val == 2:
                return 'Black'
            if val == 0:
                return 'Neither (you tied)'
            
        

def greaterScore(myGame: 'GameState'):
    '''
    Calls numColor for both black and white,
       returns a 1 if black has more pucks,
       a 2 if white has more pucks, and a 0
       if they are even
    '''
    black = myGame.numColor(len(myGame.board),
                            len(myGame.board[0]), 1)
    white = myGame.numColor(len(myGame.board),
                            len(myGame.board[0]), 2)
    if black > white:
        return 1
    elif white > black:
        return 2
    else:
        return 0

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
    myGame = GameState(board, turn, gameWin, isFull, False)
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

def sizeCorrect(num: int) -> bool:
    return num >= 4 and num <= 16

def isEven(num: int) -> bool:
    return num % 2 == 0






















