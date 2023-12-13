from collections import deque

test_uni = [
  ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'], 
  ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'], 
  ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'], 
  ['#', '.', '.', '.', '#', '.', '.', '.', '.', '.']]


with open('Day11/data.txt', 'r') as file:
  lines = file.readlines()
universe = [[char for char in line.strip()] for line in lines]


def main(uni):
  galaxy_count = sub_nums(uni) # Sub numbers for # in input
  expand_uni(uni)
  coords = get_galaxy_coords(uni, galaxy_count)
  res = 0
  for galaxy in range(1, galaxy_count):
    res += get_paths_sum(galaxy, galaxy_count, coords, uni)
  return res


def sub_nums(uni):
  ROWS = len(uni)
  COLS = len(uni[0])
  count = 1

  for r in range(ROWS):
    for c in range(COLS):
      if uni[r][c] == '#':
        uni[r][c] = str(count)
        count += 1
  return count - 1


def expand_uni(uni):
    ROWS = len(uni)
    COLS = len(uni[0])

    # Expand rows
    r = 0
    while r < ROWS:
      for c in range(COLS):
        if uni[r][c] != '.':
            break
        if c == COLS - 1:
            new_row = ['.'] * COLS
            uni.insert(r + 1, new_row)
            r += 1
            ROWS += 1  
      r += 1

    # Expand cols
    c = 0
    while c < COLS:
      for r in range(ROWS):
        if uni[r][c] != '.':
            break
        if r == ROWS - 1:
            for i in range(ROWS):
                uni[i].insert(c + 1, '.')
            c += 1
            COLS += 1  
      c += 1
    return uni


def get_galaxy_coords(uni, galaxy_count):
  ROWS = len(uni)
  COLS = len(uni[0])

  coords = [0] * (galaxy_count + 1)

  for r in range(ROWS):
    for c in range(COLS):
      if uni[r][c] != '.':
        coords[int(uni[r][c])] = (r, c)
  return coords


def get_paths_sum(start, end, coords, uni):
  # Returns sum of shortest paths from starting galaxy i to all galaxies below it
  ROWS = len(uni)
  COLS = len(uni[0])
  paths = []

  for i in range(start + 1, end + 1):
    paths.append(get_paths(coords[start], str(i), uni))
  return sum(paths)


def get_paths(coords, end, uni):
  ROWS = len(uni)
  COLS = len(uni[0])
  r = coords[0]
  c = coords[1]
  visited = set()
  q = deque()
  q.append((r, c))
  visited.add((r, c))

  length = 0
  while q:
    for i in range(len(q)):
      r, c = q.popleft()
      if uni[r][c] == end:
        return length

      directions = [[1, 0], [0, 1], [0, -1]]
      for dr, dc in directions:
        if (r + dr >= 0 and r + dr < ROWS and
            c + dc >= 0 and c + dc < COLS and
            (r + dr, c + dc) not in visited):
          q.append((r + dr, c + dc))
          visited.add((r + dr, c + dc))
    length += 1
  
  

if __name__ == "__main__":
  # print(main(universe))
  sub_nums(universe)
  expand_uni(universe)
  print(universe)