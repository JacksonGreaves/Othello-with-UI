# Jackson Greaves jdgreave

import othello_setup
from collections import namedtuple

DIRECTIONS = [[0, 1], [1, 1], [1, 0],
                  [1, -1], [0, -1], [-1, -1],
                  [-1, 0], [-1, 1]]

moveHere = namedtuple('moveHere', 'point direction moves pucksToFlip')

def takeMove(rows: int, cols: int) -> [int, int]:
    '''
    Takes the user's move as an input:
       Format: #space#
    '''
    move = str(input())
    if ' ' in move:
        moveSplit = move.split()
        moveSplit[0] = int(moveSplit[0]) - 1
        moveSplit[1] = int(moveSplit[1]) - 1
        return moveSplit

def turnToNum(item: str) -> int:
    '''
    Returns the numeric value for the current turn
    '''
    turn = 0
    if item == 'B':
        turn = 1
    if item == 'W':
        turn = 2
    return turn

def myPuckInMove(myGame: 'GameState', pucks: [int]) -> bool:
    '''
    Returns a boolean based on whether or not one of the
       current player's pucks is in a list
    '''
    if turnToNum(myGame.turn) in pucks:
        return True
    return False

def placeExists(myGame: 'GameState', row: int, col: int):
    '''
    Returns a boolean based on whether or not a
       point is on the current board
    '''
    if row in range(len(myGame.board)):
        if col in range(len(myGame.board[row])):
            return True
    return False

def adjacent(myGame: 'GameState', theTurn: int):
    '''
    Takes a GameState and returns a list of moveHere
       namedtuples containing points and directions of
       adjacent pucks
    '''
    opponentTurn = myGame.opponentColor(theTurn)
    direction = []
    delta = []
    for row in range(len(myGame.board)):
        for col in range(len(myGame.board[0])):
            for change in DIRECTIONS:
                x, y = row, col
                if myGame.isEmpty(x, y):
                    x += change[0]
                    y += change[1]
                    try:
                        if myGame.board[x][y] == opponentTurn:
                            newDirection = moveHere(point=[row, col],
                                                    direction=change, moves=[],
                                                    pucksToFlip=[])
                            delta.append(newDirection)
                    except IndexError:
                        'nothing'
    return delta

def moveCheck(myGame: 'GameState', theTurn: int):
    '''
    Takes a GameState and the turn (integer version; 1 or 2)
       and returns a list of all possible moves, their
       directions and their length
    '''
    moves = []
    answers = adjacent(myGame, theTurn)
    for delta in answers:
        newDelta = directionCheck(myGame, delta, theTurn)
        if newDelta != delta:
            moves.append(newDelta)
    return moves

def directionCheck(myGame: 'GameState', delta: 'moveHere', theTurn: int) -> 'moveHere':
    '''
    Takes a GameState, a 'moveHere' namedtuple, and
       the turn (integer version; 1 or 2) and returns
       either the original namedtuple or a new namedtuple
       containing the pucks that will be flipped
    '''
    moves = []
    pucksToFlip = []
    row = delta.point[0]
    col = delta.point[1]
    x = row
    y = col
    
    while placeExists(myGame, x, y):
        puck = myGame.board[x][y]
        moves.append(puck)
        x += delta.direction[0]
        y += delta.direction[1]
        if placeExists(myGame, x, y):
            puck = myGame.board[x][y]
            pucksToFlip.append([x,y])
        if puck == theTurn:
            moves.append(puck)
            break
    if playerTurnInList(moves, theTurn):
        if not emptyPuck(myGame, pucksToFlip):
            newDelta = moveHere(delta.point, delta.direction, moves, pucksToFlip)
            return newDelta
    return delta

def emptyPuck(myGame: 'GameState', pucks: [[int, int]]) -> bool:
    '''
    Returns a boolean based on whether or not there is an
       empty puck in a list of pucks
    '''
    for puck in pucks:
        if myGame.board[puck[0]][puck[1]] == 0:
            return True
    return False

def playerTurnInList(pucks: [[int, int]], theTurn: int) -> bool:
    '''
    Returns a boolean based on wheter or not one of the
       player's pucks is in a list of pucks
    '''
    return theTurn in pucks

def playerMoveInPossibles(delta: 'moveHere', point: [int, int]) -> bool:
    '''
    Returns a boolean based on whether the player's input
       move is in the list of possiblemoves
    '''
    return delta.point == point
    
def makeTheMove(myGame: 'GameState', moves: ['moveHere'], RandC: [int, int]):
    '''
    Takes a move and returns the list of pucks to flip
    '''
    userMove = RandC
    theMove = []
    
    while True:
        for place in moves:
            if playerMoveInPossibles(place, userMove):
                theMove.append(place)
        if theMove == []:
            print('Invalid move, please try again')
            userMove = takeMove(len(myGame.board), len(myGame.board[0]))
        else:
            break
    return theMove

def flipPucks(myGame: 'GameState', move: ['moveHere']):
    '''
    Takes a GameState and a list of moveHere namedtuples
       and flips the pucks specified in the list
    '''
    theTurn = turnToNum(myGame.turn)
    for option in move:
        myGame.board[option.point[0]][option.point[1]] = theTurn
        for point in option.pucksToFlip:
            myGame.board[point[0]][point[1]] = theTurn
    
                
                
    
        
            


