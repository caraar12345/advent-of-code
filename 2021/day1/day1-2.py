import importFile
inList = importFile.importFile('input.txt')
incDec = {'inc':0,
          'dec':0}

# TODO: Shift `lasts` to the left
# append new number, del lasts[0]

lasts = [0,0,0]
last = 0
current = 0

for x in inList:
  lasts.append(int(x))
  lasts.pop(0)
  try:
    lasts.index(0)
    pass
  except ValueError:
    for y in lasts:
      current += int(y)
    if current > last:
      incDec['inc'] += 1
    else:
      incDec['dec'] += 1



print(incDec['inc'])