import importFile
inList = importFile.importFile("input.txt")
testData = importFile.importFile("test.txt")

def removeBad(inList, bit, badBit):
    outList = []
    for num in inList:
        if num[bit] != badBit:
            outList.append(num)
    return outList

def lowestCount(inList, bit):
    count0 = 0
    count1 = 0
    for num in inList:
        if num[bit] == "1":
            count1 += 1
        else:
            count0 += 1
    return "0" if count0 > count1 else "1"


def highestCount(inList, bit):
    count0 = 0
    count1 = 0
    for num in inList:
        if num[bit] == "1":
            count1 += 1
        else:
            count0 += 1
    return "1" if count0 > count1 else "0"


def oxygenCount(inputList):
    count = 0
    while len(inputList) > 1:
        inputList = removeBad(inputList, count, highestCount(inputList, count))
        count += 1
    return int(inputList[0],base=2)


def co2Count(inputList):
    count = 0
    while len(inputList) > 1:
        inputList = removeBad(inputList, count, lowestCount(inputList, count))
        count += 1
    return int(inputList[0],base=2)

inList = testData

oxygen = oxygenCount(inList)
co2 = co2Count(inList)

print(oxygen*co2)