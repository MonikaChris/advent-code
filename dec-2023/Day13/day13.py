test = [
  ['#.##..##.',
  '..#.##.#.',
  '##......#',
  '##......#',
  '..#.##.#.',
  '..##..##.',
  '#.#.##.#.'],
  ['#...##..#',
  '#....#..#',
  '..##..###',
  '#####.##.',
  '#####.##.',
  '..##..###',
  '#....#..#']
]

test2 = [[
  '######.##',
  '##..###..',
  '.......#.',
  '#.##.#..#',
  '###.####.',
  '######..#',
  '.#..#.#.#',
  '#....###.',
  '.......##',
  '.####.##.',
  '#....#...',
  '..##....#',
  '..##....#',
  '######...',
  '.#..#..##',
  '.#..#..##',
  '######...'
]]

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
  cols = get_cols(pattern)
  if cols:
    return cols
  else:
    return get_rows(pattern) * 100


def get_cols(pattern):
  ROWS = len(pattern)
  COLS = len(pattern[0])

  pals = [[] for _ in range(ROWS)]

  for r in range(ROWS):
    for c in range(COLS - 1):
      if pattern[r][c] != pattern[r][c+1]:
        continue
      if found_palindrome(pattern[r], c):
        pals[r].append(c + 1)
  
  return get_edge(pals)


def get_rows(pattern):
  ROWS = len(pattern)
  COLS = len(pattern[0])

  pals = [[] for _ in range(COLS)]

  for c in range(COLS):
    for r in range(ROWS - 1):
      if pattern[r][c] != pattern[r+1][c]:
        continue
      if found_palindrome(get_col(pattern, c), r):
        pals[c].append(r + 1)
  
  return get_edge(pals)


def found_palindrome(line, start):
  l = start
  r = start + 1

  if r >= len(line):
    return False

  while l >= 0 and r < len(line):
    if line[l] != line[r]:
      return False
    l -= 1
    r += 1
  return True


def get_edge(arr):
  counts = {}
  for lst in arr:
    for num in lst:
      counts[num] = 1 + counts.get(num, 0)

  for key, val in counts.items():
    if val == len(arr):
      return key
  return None


def get_col(pattern, c):
  ROWS = len(pattern)
  col = []

  for r in range(ROWS):
    col.append(pattern[r][c])

  return col

  


if __name__ == "__main__":
  print(main(patterns))
  