from collections import deque

with open('Day16/data.txt', 'r') as file:
  lines = file.readlines()
lines = [line.strip() for line in lines]

with open('Day16/test.txt', 'r') as file:
  test = file.readlines()
test = [line.strip() for line in test]

with open('Day16/test2.txt', 'r') as file:
  test2 = file.readlines()
test2 = [line.strip() for line in test2]


MIRROR_R = {
  (0, -1) : [(-1, 0)],
  (-1, 0) : [(0, -1)],
  (1, 0) : [(0, 1)],
  (0, 1) : [(1, 0)]
}

MIRROR_L = {
  (0, -1) : [(1, 0)],
  (-1, 0) : [(0, 1)],
  (1, 0) : [(0, -1)],
  (0, 1) : [(-1, 0)]
}

SPLIT_V = {
  (0, -1) : [(1, 0), (-1, 0)],
  (-1, 0) : [(1, 0)],
  (1, 0) : [(-1, 0)],
  (0, 1) : [(-1, 0), (1, 0)]
}

SPLIT_H = {
  (0, -1) : [(0, 1)],
  (-1, 0) : [(0, -1), (0, 1)],
  (1, 0) : [(0, -1), (0, 1)],
  (0, 1) : [(0, -1)]
}

DOT = {
  (0, -1) : [(0, 1)],
  (-1, 0) : [(1, 0)],
  (1, 0) : [(-1, 0)],
  (0, 1) : [(0, -1)]
}


def main(grid):
  ROWS = len(grid)
  COLS = len(grid[0])
  res = 0

  # Top border
  for c in range(COLS):
    res = max(res, count_tiles(grid, [(-1, c), (0, c)]))

  # Bottom border
  for c in range(COLS):
    res = max(res, count_tiles(grid, [(ROWS, c), (ROWS-1, c)]))

  # Left border
  for r in range(ROWS):
    res = max(res, count_tiles(grid, [(r, -1), (r, 0)]))
  
  # Right border
  for r in range(ROWS):
    res = max(res, count_tiles(grid, [(r, COLS), (r, COLS-1)]))

  return res


def count_tiles(grid, start):
  energized = set()
  visited = set()
  q = deque()
  q.append(start)
  visited.add(tuple(start))

  while q:
    prev, cur = q.popleft()
    energized.add(cur)
    cells = get_next(grid, prev, cur)

    if cells:
      # cell: (new_prev, new_cur) where new_prev is old cur
      for cell in cells:
        if tuple(cell) not in visited:
          q.append(cell)
          visited.add(tuple(cell))
  return len(energized)


def get_next(grid, prev, cur):
  ROWS = len(grid)
  COLS = len(grid[0])
  pr = prev[0]
  pc = prev[1]
  cr = cur[0]
  cc = cur[1]

  found = None
  
  if grid[cr][cc] == "/":
   found = MIRROR_R[(pr - cr, pc - cc)]

  elif grid[cr][cc] == '\\':
    found = MIRROR_L[(pr - cr, pc - cc)]
  
  elif grid[cr][cc] == '|':
    found = SPLIT_V[(pr - cr, pc - cc)]
  
  elif grid[cr][cc] == '-':
    found = SPLIT_H[(pr - cr, pc - cc)]
  
  elif grid[cr][cc] == '.':
    found = DOT[(pr - cr, pc - cc)]

  if found:
    res = []
    for val in found:
      if cr + val[0] >= 0 and cr + val[0] < ROWS and cc + val[1] >= 0 and cc + val[1] < COLS:
        res.append([(cr, cc), (cr + val[0], cc + val[1])])
    return res if len(res) > 0 else None



if __name__ == "__main__":
  print(main(lines))