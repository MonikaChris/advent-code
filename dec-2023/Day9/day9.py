test_data = [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]]

with open('Day9/data.txt', 'r') as file:
  lines = file.readlines()
lines = [[int(num) for num in line.strip().split()]for line in lines]


def part1(histories):
  return main(histories, getNextVal)


def part2(histories):
  return main(histories, getPrevVal)


def main(histories, func):
  res = 0
  for hist in histories:
    res += func(hist)
  return res


def getNextVal(hist):
  rows = getRows(hist)
  res = 0
  for i in range(len(rows) - 2, -1, -1):
    res += rows[i][-1]
  return res


def getPrevVal(hist):
  rows = getRows(hist)
  res = rows[-2][0]
  for i in range(len(rows) - 3, -1, -1):
    res = rows[i][0] - res
  return res


def getRows(hist):
  rows = [hist]
  new_row = []
  all_zeros = False
  
  while not all_zeros:
    all_zeros = True
    cur_row = rows[-1]

    for i in range(1, len(cur_row)):
      val = cur_row[i] - cur_row[i-1]
      new_row.append(val)
      if val != 0:
        all_zeros = False
    rows.append(new_row)
    new_row = []
  return rows



if __name__ == "__main__":
  # print(part1(lines))
  print(part2(lines))