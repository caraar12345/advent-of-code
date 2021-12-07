from typing import Counter
import importFile
inList = importFile.importFile('input.txt')
# 12 bits to count the values
bits = {
  0: {0:0, 1:0},
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
  11: {0:0, 1:0}
}

# 12 chunks to find the leftovers
mc_chunks = {
  0: [],
  1: [],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
  8: [],
  9: [],
  10: [],
  11: []
}

lc_chunks = {
  0: [],
  1: [],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
  8: [],
  9: [],
  10: [],
  11: []
}


for binaryNum in inList:
  for x in range(len(binaryNum)):
    bits[x][int(binaryNum[x])] += 1

for x in bits.keys():
  if bits[x][0] > bits[x][1]:
    print('most common ' + str(x) + ' is 0')
    bits[x]['most common'] = '0'
    bits[x]['least common'] = '1'
  else:
    print('most common ' + str(x) + ' is 1')
    bits[x]['most common'] = '1'
    bits[x]['least common'] = '0'

for x in bits.keys():
  for y in inList:
    if y[x] != bits[x]['most common']:
      
print(len(mc_chunks[1]))