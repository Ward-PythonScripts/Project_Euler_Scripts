
#
# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
grid = "11 Euler.txt"

#
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

def GetGrid(grid):
    #get Grid
    lstGrid = []
    f = open(grid,"r")
    lstGrid.append([])
    index = 0
    doubleCount = 0
    for l in f:
        colIndex = 0
        for charac in l:
            if charac == "\n":
                index += 1
                lstGrid.append([])
            elif not charac == " ":
                if doubleCount == 0:
                    lstGrid[index].append(int(charac))
                    doubleCount += 1
                else:
                    lstGrid[index][colIndex] = int(str(lstGrid[index][colIndex]) + charac)
                    doubleCount = 0
                    colIndex += 1
    #print grid nice
    for row in lstGrid:
        print(row)
    return lstGrid


def GetBiggestValue(amountOfDigits,grid):
    biggestProduct = 1

    #Check horizontally
    for row in grid:
        for x in range(0,len(row)-amountOfDigits):
            product = 1
            for y in range(0,amountOfDigits):
                product = product * row[x+y]
            if product> biggestProduct:
                biggestProduct = product

    #Check vertically
    for col in range(0, len(grid[0])):
        for row in range(0,len(grid)-amountOfDigits):
            product = 1
            for n in range(0,amountOfDigits):
                product = product * grid[row+n][col]
            if product>biggestProduct:
                biggestProduct = product

    #Check diagonally y=x
    for row in range(0,len(grid[0])):
        for col in range(0,len(grid)):
            product = 1
            for n in range(0,amountOfDigits):
                if (row + n in range(0,len(grid[0]))) and (col+n in range(0,len(grid))):
                    product = product * grid[row+n][col+n]
            if biggestProduct<product:
                biggestProduct = product
    #Check diagonally y=-x
    for row in range(0,len(grid[0])):
        for col in range(0,len(grid)):
            product = 1
            for n in range(0,amountOfDigits):
                if (row + n in range(0,len(grid[0]))) and (col-n in range(0,len(grid))):
                    product = product * grid[row+n][col-n]
            if biggestProduct<product:
                biggestProduct = product


    return biggestProduct
print(GetBiggestValue(4,GetGrid(grid)))