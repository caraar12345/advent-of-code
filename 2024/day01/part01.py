import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from utils import import_aoc_input

aoc_input = []
for line in import_aoc_input():
    aoc_input.append([int(y) for y in line.split()])

left_list = [x[0] for x in aoc_input]
right_list = [x[1] for x in aoc_input]
left_list.sort()
right_list.sort()

total_diffs = 0

for row in range(len(aoc_input)):
    total_diffs += abs(right_list.pop(0) - left_list.pop(0))

print(total_diffs)
