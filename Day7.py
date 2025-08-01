from Utility.utility import Read, PrettyPrint

#fileData = Read("Inputs/Day7.txt")
fileData = Read("Inputs/test.txt")
fileData = fileData.splitlines()

# + and *

print(fileData)

for line in fileData:
    line = line.split()
    goal = line[0][:-1]
    numbers = line[1:]
    numSpaces = len(numbers) - 1
    for index in range(numSpaces):
        
