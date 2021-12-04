import importFile
inList = importFile.importFile('input.txt')

horizontal = 0
depth = 0
aim = 0

for command in inList:
  if command[0] == "forward":
    horizontal += command[1]
    depth += aim*command[1]
  elif command[0] == "down":
    depth += command[1]
    aim += command[1]
  elif command[0] == "up":
    depth -= command[1]
    aim -= command[1]
  print(command, depth, aim, horizontal)

print(horizontal, depth, horizontal*depth)