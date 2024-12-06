from Utility.utility import Read
import re

fileData = Read("Inputs/Day3.txt")
#fileData = Read("test.txt")

muls = re.findall(r"mul\(\d+,\d+\)", fileData)
result1 = 0
for item in muls:
    digits = re.findall(r"\d+", item)
    result1 += (int(digits[0]) * int(digits[1]))

print(f"Part 1: {result1}")
print()
parsedData = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", fileData)

filteredmuls = []
skip = False
for item in parsedData:
    if item == "don't()":
        skip = True
    elif item == "do()":
        skip = False
    elif not skip:
        filteredmuls.append(item)

result2 = 0
for item in filteredmuls:
    digits = re.findall(r"\d+", item)
    result2 += (int(digits[0]) * int(digits[1]))

print(f"Part 2: {result2}")
