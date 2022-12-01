from aocd import data

elves = data.split("\n\n")
for elf in range(len(elves)):
    elves[elf] = [int(item) for item in elves[elf].split("\n")]

elves_totals = {}
for elf in range(len(elves)):
    elves_totals[elf] = sum(elves[elf])

most_calorific = max(elves_totals, key=elves_totals.get)
print(most_calorific, elves_totals[most_calorific])
