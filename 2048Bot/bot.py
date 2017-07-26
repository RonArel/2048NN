from time import sleep
from random import *
from numpy import *

moves = [ "'w'", "'s'", "'a'", "'d'"]
recordedMoves = []
currentMove = 0
randMoveGlobal = ""
def GetBotMove(grid):
    #binaryArray = zeros(4,4)
    tempTiles = []
    tiles = []
    for item in grid:
        for num in item:
            tempTiles.append(num)
    while len(tempTiles) > 0:
        tempMax = max(tempTiles)
        tiles.append(tempMax)
        tempTiles.remove(tempMax)
    for item in range(8):
        if(2 ** item in tiles and item != 0):
            tiles.remove(2**item)
    while 0 in tiles:
        tiles.remove(0)
    i = 0
    while True:
        index =
        return GetRandMove()

def GetRandMove():
    sleep(0)
    global moves
    rand = randint(0, 3)
    return moves[rand]

def UpdateReward(reward):
    global randMoveGlobal
    global currentMove
    for item in recordedMoves:
        if(item[0] == randMoveGlobal):
            if(item[3] < reward):
                item[3] = reward
                item[1] = randMoveGlobal
            break
    else:
        recordedMoves.append((currentMove, randMoveGlobal, 0, reward))
    randMoveGlobal = ""



