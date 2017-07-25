from time import sleep
from random import *
from numpy import *

moves = [ "'w'", "'s'", "'a'", "'d'"]
def GetBotMove(grid):
    print(grid)
    tiles = []
    for i in range(4):
        for j in range(4):
           tiles.append(grid[i][j])
    x = 2
    for _ in range(11):
        if(x in tiles):
            tiles.remove(x)
        x *= 2
    indexes = zeros(4, 4)
    while True:
        maxVal = max(tiles)
        indicesList = []
        for num in range(3):
            if(maxVal in grid[num]):
                indices = [i for i, x in enumerate(grid[num]) if x == maxVal]
                for item in indices:
                    indicesList.append((num, item))
        if(len(indicesList) > 2):
            for item in indicesList:
                indexes[item[0]][item[1]] = 1
        else:
            indexes[indicesList[0][0]][indicesList[0][1]] = 1
            indexes[indicesList[1][0]][indicesList[1][1]] = 1
        #temporary
        break
    if(len(indexes) > 0):
        print("xd")
    else:
        sleep(0.1)
        global moves
        rand = randint(0, 3)
        return moves[rand]



