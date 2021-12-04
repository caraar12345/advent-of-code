import importFile
inList = importFile.importFile('input.txt')

posTotal = {
  1: {0:0, 1:0},
  2: {0:0, 1:0},
  3: {0:0, 1:0},
  4: {0:0, 1:0},
  5: {0:0, 1:0},
  6: {0:0, 1:0},
  7: {0:0, 1:0},
  8: {0:0, 1:0},
  9: {0:0, 1:0},
  10: {0:0, 1:0},
  11: {0:0, 1:0},
  12: {0:0, 1:0}
}

gammaRate = ""
epsilonRate = ""

for binaryNum in inList:
  digit = 0
  for binaryDigit in binaryNum:
    digit += 1    
    if binaryDigit == '1':
      posTotal[digit][1] += 1
    else:
      posTotal[digit][0] += 1

for pos in posTotal.keys():
  gammaVal = [key for key in posTotal[pos].items() if key[1] == max(posTotal[pos][0], posTotal[pos][1])][0][0]
  epsilonVal = [key for key in posTotal[pos].items() if key[1] == min(posTotal[pos][0], posTotal[pos][1])][0][0]
  gammaRate += str(gammaVal)
  epsilonRate += str(epsilonVal)

print(int(gammaRate, 2)*int(epsilonRate, 2))