from aocd import data

#data = "A Y\nB X\nC Z"

mapElf = {"A":"Rock", "B":"Paper", "C":"Scissors"}
mapMe  = {"X":"Rock", "Y":"Paper", "Z":"Scissors"}
mapMeScore = {"Rock": 1, "Paper": 2, "Scissors": 3}

combos = {("Rock",    "Paper"):     6,
          ("Paper",   "Scissors"):  6,
          ("Scissors","Rock"):      6,

          ("Rock",    "Scissors"):  0,
          ("Paper",   "Rock"):      0, 
          ("Scissors","Paper"):     0,

          ("Rock",    "Rock"):      3,
          ("Paper",   "Paper"):     3,
          ("Scissors","Scissors"):  3}

pairs = [pair.split(" ") for pair in data.splitlines()]

total = 0
for pair in pairs:
  outcomeScore = combos[mapElf[pair[0]], mapMe[pair[1]]]
  choiceScore = mapMeScore[mapMe[pair[1]]]
  total += outcomeScore + choiceScore

print(total)