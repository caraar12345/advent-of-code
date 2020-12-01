file=open("input.txt","r")
fileArray = file.readlines()
final = []
for x in fileArray:
    final.append(x.strip())

twoCount = 0
threeCount = 0

for id in final:
    letters = []
    counts = dict()
    for letter in id:
        counts[letter] = counts.get(letter,0)+1
    two = False
    three = False
    for x in counts.values():
        if x == 2 and two == False:
            twoCount += 1
            two = True
        elif x == 3 and three == False:
            threeCount += 1
            three = True

print(twoCount*threeCount)
