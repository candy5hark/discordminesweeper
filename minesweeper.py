from random import *



dimension = int(input("Dimensions: "))
bombs = int(input("Number of bombs: "))
gridSize = dimension*dimension
grid = []

while bombs > gridSize:
    bombs = int(input("Number of !possible! bombs: "))

chance_to_place = bombs / gridSize

print(chance_to_place)

i = 0
while i < gridSize :
    grid.append(":white_medium_square:")
    i += 1

i = 0
bombsPlaced = 0
while i < gridSize:
    if chance_to_place > random() and grid[i] == ":white_medium_square:" and bombsPlaced < bombs:
        grid[i] = ":bomb:"
        bombsPlaced += 1
    i += 1
    if i >= gridSize and bombsPlaced < bombs:
        i = 0

i = 0
surroundingBombs = 0



while i < gridSize:
    surroundingBombs = 0

    if i % dimension == 0:
        leftEdge = True
    else:
        leftEdge = False

    if i % dimension == dimension -1:
        rightEdge = True
    else:
        rightEdge = False

    if i < dimension:
        topRow = True
    else:
        topRow = False

    if i >= gridSize - dimension:
        bottomRow = True
    else:
        bottomRow = False

#up left
    if not topRow and not leftEdge and i > dimension and grid[i - dimension - 1] == ":bomb:":
        surroundingBombs += 1
#up
    if not topRow and grid[i - dimension] == ":bomb:":
        surroundingBombs += 1
#up right
    if not topRow and not rightEdge and grid[i - dimension + 1] == ":bomb:":
        surroundingBombs += 1
#left
    if not leftEdge and grid[i - 1] == ":bomb:":
        surroundingBombs += 1
#right
    if not rightEdge and grid[i + 1] == ":bomb:":
        surroundingBombs += 1
#bottom left
    if not bottomRow and not leftEdge and grid[i + dimension - 1] == ":bomb:":
        surroundingBombs += 1
#bottom
    if not bottomRow and grid[i + dimension] == ":bomb:":
        surroundingBombs += 1
#bottom right
    if not bottomRow and not rightEdge and grid[i + dimension + 1] == ":bomb:":
        surroundingBombs += 1

    if grid[i] == ":white_medium_square:":
        if surroundingBombs == 1:
            grid[i] = ":one:"
        if surroundingBombs == 2:
            grid[i] = ":two:"
        if surroundingBombs == 3:
            grid[i] = ":three:"
        if surroundingBombs == 4:
            grid[i] = ":four:"
        if surroundingBombs == 5:
            grid[i] = ":five:"
        if surroundingBombs == 6:
            grid[i] = ":six:"
        if surroundingBombs == 7:
            grid[i] = ":seven:"
        if surroundingBombs == 8:
            grid[i] = ":eight:"

    i += 1


i = 0
iterator = 0

while i < gridSize:
    print("||", end='')
    print(grid[i], end='')
    print("||", end='')
    i += 1
    if i % dimension == 0:
        print("")

