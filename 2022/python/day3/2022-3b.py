from aocd import data

rucksacks = [rucksack for rucksack in data.splitlines()]

groups = [
    [rucksacks[x], rucksacks[x + 1], rucksacks[x + 2]]
    for x in range(0, len(rucksacks), 3)
]


priorities = 0
for group in groups:
    for item_type in group[0]:
        if item_type in group[1] and item_type in group[2]:
            if ord(item_type) > 96:
                priority = ord(item_type) - 96
            elif ord(item_type) < 96:
                priority = ord(item_type) - 38
    priorities += priority

print(priorities)
