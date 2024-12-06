from Utility.utility import Read

fileData = Read("Inputs/Day4.txt")
#fileData = Read("Inputs/test.txt")

grid = fileData.splitlines()
numRows = len(grid)
numCols = len(grid[0])
count = 0

for row in range(numRows):
    for col in range(numCols):
        if grid[row][col] == "X":
            # N
            if row >= 3 and (grid[row-1][col] == "M" and grid[row-2][col] == "A" and grid[row-3][col] == "S"):
                #print(f"N[{row}][{col}]")
                count += 1
            # NE
            if row >= 3 and col < numCols - 3 and  (grid[row-1][col+1] == "M" and grid[row-2][col+2] == "A" and grid[row-3][col+3] == "S"):
                #print(f"NE[{row}][{col}]")
                count += 1
            # E
            if col < numCols - 3 and (grid[row][col+1] == "M" and grid[row][col+2] == "A" and grid[row][col+3] == "S"):
                #print(f"E[{row}][{col}]")
                count += 1
            # SE
            if row < numRows - 3 and col < numCols - 3 and (grid[row+1][col+1] == "M" and grid[row+2][col+2] == "A" and grid[row+3][col+3] == "S"):
                #print(f"SE[{row}][{col}]")
                count += 1
            # S
            if row < numRows - 3 and (grid[row+1][col] == "M" and grid[row+2][col] == "A" and grid[row+3][col] == "S"):
                #print(f"S[{row}][{col}]")
                count += 1
            # SW
            if row < numRows - 3 and col >= 3 and (grid[row+1][col-1] == "M" and grid[row+2][col-2] == "A" and grid[row+3][col-3] == "S"):
                #print(f"SW[{row}][{col}]")
                count += 1
            # W
            if col >= 3 and (grid[row][col-1] == "M" and grid[row][col-2] == "A" and grid[row][col-3] == "S"):
                #print(f"W[{row}][{col}]")
                count += 1
            # NW
            if row >= 3 and col >= 3 and (grid[row-1][col-1] == "M" and grid[row-2][col-2] == "A" and grid[row-3][col-3] == "S"):
                #print(f"NW[{row}][{col}]")
                count += 1
                
print(f"Part 1: {count}")

count = 0

for row in range(1, numRows - 1):
    for col in range(1, numCols - 1):
        if grid[row][col] == "A":
            instance = 0
            if grid[row-1][col-1] == "M" and grid[row+1][col+1] == "S":
                instance += 1

            if grid[row+1][col+1] == "M" and grid[row-1][col-1] == "S":
                instance += 1
            
            if grid[row+1][col-1] == "M" and grid[row-1][col+1] == "S":
                instance += 1
            
            if grid[row-1][col+1] == "M" and grid[row+1][col-1] == "S":
                instance += 1
            
            if instance == 2:
                count += 1
                
print(f"Part 2: {count}")