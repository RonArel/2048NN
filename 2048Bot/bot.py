from time import sleep
from random import *
from numpy import *

moves = [ "'w'", "'s'", "'a'", "'d'"]
recordedMoves = []
currentMove = 0
randMoveGlobal = ""
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
                        randnum = randint(item[2])
                        if(randnum == 0):
                            item[2] += 1
                            return item[1]
                        else:
                            return GetRandMove()
                    else:
                        randMove = GetRandMove()
                        global randMoveGlobal
                        # recordedMoves.append((((maxVals[j])(maxVals[j + 1])), randMove, 0, 0))
                        randMoveGlobal = randMove
                        global currentMove
                        currentMove = ((maxVals[j])(maxVals[j + 1]))
                        return randMove
            elif(maxVals[j][1] == maxVals[j + 1][1]):
                for item in recordedMoves:
                    if(item[0] == (maxVals[j])(maxVals[j + 1])):
                        return item[1]
                    else:
                        randMove = GetRandMove()
                        #recordedMoves.append((((maxVals[j])(maxVals[j + 1])), randMove, 0, 0))
                        randMoveGlobal = randMove
                        currentMove = ((maxVals[j])(maxVals[j + 1]))
                        return randMove
            else:
                if(maximum > 3):
                    maximum /= 2
                else:
                    break
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



