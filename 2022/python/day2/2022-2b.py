from aocd import data

#data = "A Y\nB X\nC Z"

mapElf = {"A":"Rock", "B":"Paper", "C":"Scissors"}
mapMe  = {"X": "Lose", "Y": "Draw", "Z": "Win"}
mapMeScore = {"Rock": 1, "Paper": 2, "Scissors": 3}
mapOCScore = {"Win": 6, "Draw": 3, "Lose": 0}

combos = {("Rock",    "Paper"):     6,
          ("Paper",   "Scissors"):  6,
          ("Scissors","Rock"):      6,

          ("Rock",    "Scissors"):  0,
          ("Paper",   "Rock"):      0, 
          ("Scissors","Paper"):     0,

          ("Rock",    "Rock"):      3,
          ("Paper",   "Paper"):     3,
          ("Scissors","Scissors"):  3}

newCombos = {"Win":  {"Rock":"Paper",    "Paper":"Scissors", "Scissors": "Rock"},
             "Lose": {"Rock":"Scissors", "Paper":"Rock",     "Scissors":"Paper"}}

pairs = [pair.split(" ") for pair in data.splitlines()]

total = 0
for pair in pairs:
  elf = mapElf[pair[0]]
  outcome = mapMe[pair[1]]
  if outcome == "Draw":
    my_choice = mapElf[pair[0]]
  else:
    my_choice = newCombos[outcome][elf]
  my_choice_score = mapMeScore[my_choice]
  total += mapOCScore[outcome] + my_choice_score

print(total)