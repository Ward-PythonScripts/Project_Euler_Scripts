
#


# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?
import itertools

def amountOfRoutes(grid):
    #we can go down and left, the order in which we do these steps determines the path
    sum  = 0
    for n in range(1,grid+2):
        print(n)

        paths = 2**n
        print("In between paths " + str(paths))

        badPaths = 2**(n-2)
        print("In between badPaths " + str(badPaths))

        print("********************************************************")
    return (paths - badPaths)
#print(amountOfRoutes(20))

def nicePrint(grid):
    for row in grid:
        print(row)

def mattis(limit):
    grid = [[1]*(limit +1)]
    for x in range(limit):
        grid += [[1] + [0] * limit]
    nicePrint(grid)
    print("#"*100)
    for x in range(0,limit+1):
        for y in range(0,limit+1):
            if grid[x][y] == 0:
                grid[x][y] = grid[x-1][y] + grid[x][y -1]
    nicePrint(grid)
mattis(20)