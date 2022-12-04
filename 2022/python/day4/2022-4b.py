from aocd import lines
# testData = """2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8"""

# lines = testData.splitlines()

pairs = []
for pair in lines:
    pair = pair.split(",")
    elfPair = []
    for elf in pair:
        elfPair.append([int(num) for num in elf.split("-")])
    pairs.append(elfPair)

intersectionCount = 0
for pair in pairs:
    set1 = {x for x in range(pair[0][0], pair[0][1]+1)}
    set2 = {x for x in range(pair[1][0], pair[1][1]+1)}
    if set1.intersection(set2):
        intersectionCount += 1

print(intersectionCount)
