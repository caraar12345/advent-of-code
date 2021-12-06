def importFile(inFile):
  with open(inFile, 'r') as f:
    file = []
    for line in f.readlines():
      file.append(line.strip())
    return file

inputFile = importFile('input.txt')

bingo_cards = []

for line in range(len(inputFile)):
  currentLine = inputFile[line]
  if line == 0:
    bingo_calls = currentLine.split(',')
    continue
  elif len(currentLine) == 0:
    print(0)
    pass
  elif len(currentLine.split(" ")) > 5:
    print(currentLine.split(" "))
    for item in inputFile[line]:
      if len(item) == 0:
        currentLine.remove(item)
  bingo_cards.append(currentLine)

print(bingo_calls)
print(bingo_cards)