from importFile import *

inFileList = importFile("input.txt")

for number in inFileList:
    for secNum in inFileList:
        for triNum in inFileList:
            if number + secNum + triNum == 2020:
                print(number, secNum, triNum)
                print(number*secNum*triNum)
                quit()
