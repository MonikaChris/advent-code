test = [[
  '#.##..##.',
  '..#.##.#.',
  '##......#',
  '##......#',
  '..#.##.#.',
  '..##..##.',
  '#.#.##.#.'],
  [
  '#...##..#',
  '#....#..#',
  '..##..###',
  '#####.##.',
  '#####.##.',
  '..##..###',
  '#....#..#']
]

with open('Day13/data.txt', 'r') as file:
  lines = file.readlines()
lines = [line.strip() for line in lines]
patterns = []
pattern = []
for line in lines:
  if line:
    pattern.append(line)
  else:
    patterns.append(pattern)
    pattern = []
if pattern:
  patterns.append(pattern)


def main(patterns):
  res = 0
  for pattern in patterns:
    res += get_reflection(pattern)
  return res

def get_reflection(pattern):
  cols = get_mirror(rotate(pattern))
  if cols:
    return cols
  else:
    rows = get_mirror(pattern) * 100
    return rows


def get_mirror(pattern):
  # Make grid of row index by row index where element is number of characters that differ
  ROWS = len(pattern)
  grid = [[0 for _ in range(ROWS)] for _ in range(ROWS)]
  
  for r in range(ROWS):
    for c in range(ROWS):
      grid[r][c] = get_diff(pattern, r, c)
  return find_line(grid)
  

def get_diff(pattern, i, j):
  row1 = pattern[i]
  row2 = pattern[j]

  count = 0
  for i in range(len(row1)):
    if row1[i] != row2[i]:
      count += 1
  return count
  

def find_line(grid):
  # Check odd diagonals, look for sum of 2 (1 double counted)
  ROWS = len(grid)

  diagonals = [[] for _ in range(ROWS * 2 - 1)]
  for r in range(ROWS):
    for c in range(ROWS):
      if (r + c) % 2 == 1:
        diagonals[r + c].append(grid[r][c])
  
  for i, arr in enumerate(diagonals):
    if sum(arr) == 2:
      return i//2 + 1
  return None


def rotate(grid):
  ROWS = len(grid)
  COLS = len(grid[0])

  new_grid = []

  for c in range(COLS):
    new_row = []
    for r in range(ROWS):
      new_row.append(grid[r][c])
    new_grid.append(new_row)

  return new_grid



if __name__ == "__main__":
  print(main(patterns))
  
  