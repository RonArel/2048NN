from time import sleep
from random import *
from numpy import *

moves = [ "'w'", "'s'", "'a'", "'d'"]
recordedMoves = []
currentMove = 0
randMoveGlobal = ""
def GetBotMove(grid):
    binaryArray = grid
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
        for item in binaryArray:
            for num in item:
                num -= tiles[i] - 1
        sumX = sum(binaryArray, axis=1)
        sumY = sum(binaryArray, axis=0)
        print(binaryArray)
        if(2 in sumX):
            lSumX = []
            for item in sumX:
                lSumX.append(item)
            lSumX.index(2)
        elif(2 in sumY):
            lSumY = []
            for item in sumY:
                lSumY.append(item)
            lSumY.index(2)
        elif(i > len(tiles) - 2):
            return GetRandMove()
        else:
            i += 1

def GetRandMove():
    sleep(0)
    global moves
    rand = randint(0, 3)
    return moves[rand]

def UpdateReward(reward):
    pass



