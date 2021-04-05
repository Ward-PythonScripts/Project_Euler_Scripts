
#
# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
print("Which file ?, no need to use quotation marks")
grid = input("file name = ")
print("How many to group?")
group = int(input("amount to group = "))

#
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

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
                doubleCount += 1
                if doubleCount==group:
                    doubleCount = 0
                    colIndex += 1
#print grid nice
print(lstGrid)
input("Press enter to close application")

