from aocd import data

elves = data.split("\n\n")
for elf in range(len(elves)):
    elves[elf] = [int(item) for item in elves[elf].split("\n")]

elves_totals = {}
for elf in range(len(elves)):
    elves_totals[elf] = sum(elves[elf])

most_calorific = dict(sorted(elves_totals.items(), key=lambda item: item[1]))
top_3 = list(most_calorific.keys())[-3:]

y = 0
for x in top_3:
    y += most_calorific[x]

print(y)