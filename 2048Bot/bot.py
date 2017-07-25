from time import sleep
from random import *
from numpy import *

moves = [ "'w'", "'s'", "'a'", "'d'"]
recordedMoves = []
def GetBotMove(grid):
    maxlist = []
    for item in range(3):
        maxlist.append(max(grid[item]))
    maximum = max(maxlist)
    while True:
        maxVals = []
        x = 0
        for i in grid:
            if(maximum in i):
                val = argwhere(maximum)
                maxVals.append((x, val))
            x += 1
        for j in range(len(maxVals) - 1):
            if(maxVals[j][0] == maxVals[j + 1][0]):
                for item in recordedMoves:
                    if(item[0] == ((maxVals[j])(maxVals[j + 1]))):
                        return item[1]
                    else:
                        randMove = GetRandMove()
                        recordedMoves.append((((maxVals[j])(maxVals[j + 1])), randMove, 0))
                        return randMove
            elif(maxVals[j][1] == maxVals[j + 1][1]):
                for item in recordedMoves:
                    if(item[0] == ((maxVals[j])(maxVals[j + 1]))):
                        return item[1]
                    else:
                        randMove = GetRandMove()
                        recordedMoves.append((((maxVals[j])(maxVals[j + 1])), randMove, 0))
                        return randMove
            else:
                return GetRandMove()
        break

def GetRandMove():
    sleep(0.1)
    global moves
    rand = randint(0, 3)
    return moves[rand]


