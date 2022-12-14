from aocd import data

diagram = data.split(" 1   2   3   4   5   6   7   8   9 \n")[0].strip("\n")
instructions = data.split(" 1   2   3   4   5   6   7   8   9 \n")[1].strip("\n").splitlines()

rows = []
for line in diagram.splitlines():
    row = []
    for crate in range(1, len(line), 4):
        row.append(line[crate])
    rows.append(row)

columns = [list(tup) for tup in zip(*rows[::-1])]

col_dict = {i+1: columns[i] for i in range(9)}
print(col_dict)
print(col_dict[4])
print(col_dict[4].pop())
print(col_dict[4])
print(instructions)