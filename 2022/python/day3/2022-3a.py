from aocd import data

rucksacks = [
    [rucksack[int(len(rucksack) / 2) :], rucksack[: int(len(rucksack) / 2)]]
    for rucksack in data.splitlines()
]


priorities = 0
for rucksack in rucksacks:
    for letter in rucksack[0]:
        if letter in rucksack[1]:
            if ord(letter) > 96:
                priority = ord(letter) - 96
            elif ord(letter) < 96:
                priority = ord(letter) - 38
    priorities += priority

print(priorities)
