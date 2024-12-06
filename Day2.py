from Utility.utility import Read

def checkSafety(report):
    safe = True

    for i in range(1, len(report)):
        difference = int(report[i]) - int(report[i-1])
        if(i == 1):
            if difference > 0:
                increasing = True
            else:
                increasing = False

        if (difference > 0 and not increasing) or (difference <= 0 and increasing):
            safe = False
            break
        if abs(difference) < 1 or abs(difference) > 3:
            safe = False
            break
    return safe


fileData = Read("Inputs/Day2.txt")
#fileData = Read("test.txt")
reports = []

fileData = fileData.split("\n")

safeCount = 0
unsafeReports = []

for line in fileData:

    report = line.split()
    
    safe = checkSafety(report)
    
    if safe:
        safeCount += 1
    else:
        unsafeReports.append(report)

print(f"Part 1: {safeCount}")

for report in unsafeReports:
    possibleReports = []
    for i in range(len(report)):
        temp = []
        for j in range(len(report)):
            if j != i:
                temp.append(report[j])
        possibleReports.append(temp)
    
    for possibleReport in possibleReports:
        safe = checkSafety(possibleReport)
        if safe:
            safeCount += 1
            break


print(f"Part 2: {safeCount}")
