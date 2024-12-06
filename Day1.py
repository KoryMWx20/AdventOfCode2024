from Utility.utility import Read

fileData = Read("Inputs/Day1.txt")
fileData = fileData.split()
leftList = []
rightList = []
for index, num in enumerate(fileData):
    if index % 2 == 0:
        leftList.append(int(num))
    else:
        rightList.append(int(num))

sum = 0

leftList.sort()
rightList.sort()

for i in range(len(leftList)):
    sum += abs(rightList[i] - leftList[i]) 

print("Part 1: " + str(sum))

score = 0

for num in leftList:
    score += (num * rightList.count(num))

print("Part 2: " + str(score))