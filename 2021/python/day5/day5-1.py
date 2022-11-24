import importFile

def boardGen(width, height):
    board = [[0 for x in range(width)] for y in range(height)]
    return board

coordList = importFile.importFile('input.txt')
horiVerti = []
for y in coordList:
  if y[0][0] == y[1][0] or y[0][1] == y[1][1]:
    horiVerti.append(y)

board = boardGen(1000, 1000)
count1 = 0
for vector in horiVerti:
  for x in range(vector[0][0], vector[1][0]):
    print(vector[0][0], vector[1][0], vector[0][1], vector[1][1])

    for y in range(vector[0][1], vector[1][1]):
      print(x,y)

for x in range(1000):
  for y in range(1000):
    if board[x][y] > 1:
      count1 += 1

print(count1)