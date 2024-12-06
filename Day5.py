from Utility.utility import Read

fileData = Read("Inputs/Day5.txt")
#fileData = Read("Inputs/test.txt")

sections = fileData.split("\n\n")
topSection = sections[0].splitlines()
bottomSection = sections[1].splitlines()

rules = dict()
for line in topSection:
    pair = line.split("|")
    key = pair[0]
    value = pair[1]
    rules.setdefault(key, []).append(value)

validUpdates = []
invalidUpdates = []

def validate(pages):
    for index, page in enumerate(pages):
        if page in rules:
            for i in range(index, -1, -1):
                if pages[i] in rules[page]:
                    return False
                
    return True
                    
sum = 0
for line in bottomSection:
    pages = line.split(",")
    if validate(pages):
        sum += int(pages[len(pages) // 2])    

print(f"Part 1: {sum}")

def sorting(a, b):
    if a in rules:
        entry = rules[a]
        if b in entry:
            return -1
        return 1
    return 1

sum = 0
fixedUpdates = []
for line in bottomSection:
    pages = line.split(",")
    if not validate(pages):
        valid = False
        while not valid:
            for index, page in enumerate(pages):
                if page in rules:
                    for i in range(index, -1, -1):
                        if pages[i] in rules[page]:
                            temp = pages.pop(i)
                            pages.insert(index+1, temp)
            valid = validate(pages)
        sum += int(pages[len(pages) // 2])
    
print(f"Part 2: {sum}")
