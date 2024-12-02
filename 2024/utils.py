def import_aoc_input() -> list:
    final = []
    with open("input.txt") as f:
        for line in f.readlines():
            final.append(line.strip())
    return final
