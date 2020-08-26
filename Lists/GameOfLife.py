"""
Supposed to be a program that looks at the neighbours of the cell and if 2 or 3 exist then it stays alive
if the cell is already dead but has 3 neighhours that are alive it will come alive
Else if it is alive or dead but does not contain the above requirements it will be set to dead

"""
import random, time, copy

WIDTH = 60
HEIGHT = 20

nextCells = []                                          # List of list for cells

for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#')                          # adds a living cell
        else:
            column.append(' ')                          # adds a dead cell
    nextCells.append(column)                            # nextcells is now a list of columns

while True:
    print('\n\n\n\n')                               # seperates each step with newlines
    currentCells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')           # prints the # or empty string
        print()                                         #new line at end of row

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighbouring coords
            # ' % WIDTH ' will always be between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # count number of living neighbours
            numBours = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numBours += 1                           # top left is alive
            if  currentCells[x][aboveCoord] == '#':
                numBours += 1                           # above
            if currentCells[rightCoord][aboveCoord] == '#':
                numBours += 1                           # top right
            if currentCells[rightCoord][y] == '#':
                numBours += 1                           # right
            if currentCells[rightCoord][belowCoord] == '#':
                numBours += 1                           # bottom right
            if currentCells[x][belowCoord] == '#':
                numBours += 1                           # bottom
            if currentCells[leftCoord][belowCoord] == '#':
                numBours += 1                           # bottom left
            if currentCells[leftCoord][y] == '#':
                numBours += 1                           # left
            
            # 2 or 3 neighbours stay alive
            if currentCells[x][y] == '#' and (numBours == 2 or numBours == 3):
                nextCells[x][y] = '#' 
            # dead cells with 3 neighbours come alive
            elif currentCells[x][y] == ' ' and numBours == 3:
                nextCells[x][y] == '#'
            # everything else dies or stays dead
            else:
                nextCells[x][y] == ' '
            
    time.sleep(1)