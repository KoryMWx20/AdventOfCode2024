from Utility.utility import Read, PrettyPrint

fileData = Read("Inputs/Day6.txt")
#fileData = Read("Inputs/test.txt")

fileData = fileData.splitlines()
grid = []
for line in fileData:
    grid.append(list(line))
numRows = len(grid)
numCols = len(grid[0])

done = False
for row in range(numRows):
        for col in range(numCols):
            if grid[row][col] == "^":
                guard = (row, col)
                break

while not done:
    # move up
    movement = 0
    while grid[guard[0]-movement][guard[1]] != "#":
        grid[guard[0]-movement][guard[1]] = "X"
        movement += 1
        if guard[0]-movement < 0:
            done = True
            break
    if done:
        break
    guard = (guard[0]-movement+1, guard[1])
    # move right
    movement = 0
    while grid[guard[0]][guard[1]+movement] != "#":
        grid[guard[0]][guard[1]+movement] = "X"
        movement += 1
        if guard[1]+movement >= numCols:
            done = True
            break
    if done:
        break
    guard = (guard[0], guard[1]+movement-1)
    # move down
    movement = 0
    while grid[guard[0]+movement][guard[1]] != "#":
        grid[guard[0]+movement][guard[1]] = "X"
        movement += 1
        if guard[0]+movement >= numRows:
            done = True
            break
    if done:
        break
    guard = (guard[0]+movement-1, guard[1])
    # move left
    movement = 0
    while grid[guard[0]][guard[1]-movement] != "#":
        grid[guard[0]][guard[1]-movement] = "X"
        movement += 1
        if guard[1]-movement < 0:
            done = True
            break
    if done:
        break
    guard = (guard[0], guard[1]-movement+1)

count = 0
for row in range(numRows):
        for col in range(numCols):
            if grid[row][col] == "X":
                count += 1

print(f"Part 1: {count}")
