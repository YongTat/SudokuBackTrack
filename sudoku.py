GRID = [
    [0,7,0,0,0,0,4,0,5],
    [0,0,0,0,0,1,0,0,6],
    [2,0,0,0,7,0,0,0,0],
    [0,0,4,2,0,0,0,0,8],
    [0,0,0,7,0,0,0,1,0],
    [1,3,0,0,0,5,0,0,9],
    [0,0,0,5,0,0,1,0,0],
    [9,0,0,3,0,0,0,6,0],
    [6,0,0,0,0,0,0,0,4]
]

def solver(grid):
    """[Sovle sudoku with given grid]

    Args:
        grid ([2D Array]): 2D Matrix to represent sudoku grid

    Returns:
        [Boolean]: [Boolean for recursion]
    """
    nextpos = findEmpty(grid)
    if nextpos == False:
        return True
    else:
        row, col = nextpos
    
    for i in range(1,10):
        if checkdigit(grid,i,(row,col)):
            grid[row][col] = i

            if solver(grid):
                return True

            grid[row][col] = 0

    return False

def findEmpty(grid):
    """[Find next 0 in grid]

    Args:
        grid ([2D Array]): 2D Matrix to represent sudoku grid

    Returns:
        (Y,X): positon of next 0 in grid
        False: if no 0 found
    """
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i,j) # returns a tuple in (Y,X) format
    
    return False

def checkdigit(grid, num, pos):
    """[summary]

    Args:
        grid ([2D Array]): 2D Matrix to represent sudoku grid
        num ([int]): Number to be inserted into the grid
        pos ([(Y,X)]): position to insert given number

    Returns:
        [Boolean]: [False if dupe found else True]
    """
    #check row
    for i in range(9):
        if num == grid[pos[0]][i] and pos[1] != i: #checks row for dupe and skips current position
            return False

    #check colum
    for i in range(9):
        if num == grid[i][pos[1]] and pos[0] != i: # check colum for dupe and skips current position
            return False

    #Check 9x9
    getbox_x = pos[1] // 3
    getbox_y = pos[0] // 3

    for i in range(getbox_y * 3, getbox_y * 3 + 3):
        for j in range(getbox_x * 3, getbox_x * 3 + 3):
            if grid[i][j] == num and (i,j) != pos:
                return False

    return True

def showGrid(grid):
    """[Prints sudoku onto console in a pretty way]

    Args:
        grid ([2D Array]): 2D Matrix to represent sudoku grid
    """
    for i in range(len(grid)): #i is Y axis
        if i % 3 == 0 and i != 0:
            print("~~~~~~~~~~~~~~~~~~~~~~~~")

        for j in range(len(grid[1])): #j is x axis
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(str(grid[i][j]))
            else:
                print(str(grid[i][j]) + " ", end="")

    print("")

showGrid(GRID)
solver(GRID)
showGrid(GRID)
