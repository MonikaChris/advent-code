test_data = [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]]


with open('Day9/data.txt', 'r') as file:
  lines = file.readlines()
lines = [[int(num) for num in line.strip().split()]for line in lines]


def main(histories):
  res = 0
  for hist in histories:
    res += getNextVal(hist)
  return res


def getNextVal(hist):
  rows = getRows(hist)
  res = 0
  for i in range(len(rows) - 2, -1, -1):
    res += rows[i][-1]
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
  print(main(lines))