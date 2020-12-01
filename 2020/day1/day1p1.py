from importFile import *

inFileList = importFile("input.txt")

for number in inFileList:
    for secNum in inFileList:
        if number + secNum == 2020:
            print(number, secNum)
            print(number*secNum)
            quit()
