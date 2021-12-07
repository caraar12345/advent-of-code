def import_file(in_file):
  with open(in_file, 'r') as f:
    file = []
    for line in f.readlines():
      file.append(line.strip())
    return file

input_file = import_file('input.txt')

bingo_cards_numbers = [[]]
bingo_cards_dobbings = []
bingo_calls = list(map(int, input_file.pop(0).split(",")))
input_file.pop(0)
card_counter = 0
row_counter = 0
for line in input_file:
  if line.split(" ") == ['']:
    bingo_cards_numbers.append([])
    continue

  bingo_cards_numbers[card_counter].append([])

  for num in line.split(" "):
    if num == '':
      continue
    else:
      bingo_cards_numbers[card_counter][row_counter].append(int(num))
  row_counter += 1

  if row_counter == 5:
    card_counter += 1
    row_counter = 0
    continue

bingo_cards_numbers.reverse()

for card in bingo_cards_numbers:
  for row in card:
    print(row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\t", row[4])
  print("\n")

for card in range(len(bingo_cards_numbers)):
  bingo_cards_dobbings.append(
    [['','','','',''],
     ['','','','',''],
     ['','','','',''],
     ['','','','',''],
     ['','','','','']])

for call in bingo_calls:
  for card in range(len(bingo_cards_numbers)):
    for row in range(len(bingo_cards_numbers[card])):
      if call in bingo_cards_numbers[card][row]:
        bingo_cards_dobbings[card][row][bingo_cards_numbers[card][row].index(call)] = 'X'
        #print(bingo_cards_numbers[card][row])
        print("\n")
        print(bingo_cards_dobbings[card])

        if bingo_cards_dobbings[card][row] == ['X','X','X','X','X']:
          winning_card_num = card
          winning_card = bingo_cards_numbers[card]
          print("row", winning_card_num)
          print(winning_card)
          final_val = 0
          for row in winning_card:
            row_ref = 0
            col_ref = 0
            for num in row:
              if bingo_cards_dobbings[row_ref][col_ref] == 'X':
                col_ref += 1
                continue
              else: 
                final_val += num
                col_ref += 1
            row_ref += 1
          final_val = final_val * call
          print(final_val)
          print(call)
          quit()

        for col in zip(*bingo_cards_dobbings[card]):
          if col == ['X','X','X','X','X']:
            winning_card_num = card
            winning_card = bingo_cards_numbers[card]
            print("col", winning_card_num)
            print(winning_card)
            final_val = 0
            for row in winning_card:
              row_ref = 0
              col_ref = 0
              for num in row:
                if bingo_cards_dobbings[row_ref][col_ref] == 'X':
                  col_ref += 1
                  continue
                else: 
                  final_val += num
                row_ref += 1
            final_val = final_val * call
            print(final_val)

            quit()

### TOTALLY AND UTTERLY CLICKOPSED ###
# >>> card = [[64, 65, 6, 86, 53], [10, 56, 2, 88, 73], [11, 62, 37, 84, 1], [71, 42, 76, 51, 77], [41, 83, 19, 14, 4]]
# >>> final_val = 0
# >>> for row in card:
# ...   for col in row:
# ...     final_val += col
# ... 
# >>> final_val
# 1176
# >>> final_val -= 73
# >>> final_val -= 62
# >>> final_val -= 37
# >>> final_val -= 1
# >>> final_val -= 71
# >>> final_val -= 42
# >>> final_val -= 76
# >>> final_val -= 51
# >>> final_val -= 77
# >>> final_val -= 41
# >>> final_val -= 83
# >>> final_val
# 562
# >>> final_val * 71
# 39902