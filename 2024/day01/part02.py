import os
import sys
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from utils import import_aoc_input

aoc_input = []
for line in import_aoc_input():
    aoc_input.append([int(y) for y in line.split()])

left_list = [x[0] for x in aoc_input]
right_list = [x[1] for x in aoc_input]
left_list.sort()
right_list.sort()

sim_score = 0
counter = Counter(right_list)
print(counter)
for number in left_list:
    sim_score += number * counter[number]

print(sim_score)
