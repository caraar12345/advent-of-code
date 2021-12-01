import importFile
inList = importFile.importFile('input.txt')
incDec = {'inc':0,
          'dec':0}
last = 0
for x in inList:
  if int(x) > last:
    incDec['inc'] += 1
  else:
    incDec['dec'] += 1
  last = int(x)

print(incDec['inc']-1)