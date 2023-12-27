from collections import deque

with open('Day16/data.txt', 'r') as file:
  lines = file.readlines()
lines = [line.strip() for line in lines]

with open('Day16/test.txt', 'r') as file:
  test = file.readlines()
test = [line.strip() for line in test]

with open('Day16/test3.txt', 'r') as file:
  test3 = file.readlines()
test3 = [line.strip() for line in test3]




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

def main(grid, grid2):
  ROWS = len(grid)
  COLS = len(grid[0])
  grid2 = [list(word) for word in grid2]
  energized = set()
  visited = set()
  q = deque()
  q.append([(0, 0), (0, 1)])
  energized.add((0, 0))

  while q:
    prev, cur = q.popleft()
    # print(f'cur: {cur}')
    energized.add(cur)
    visited.add((prev, cur))
    grid2[cur[0]][cur[1]] = "X"
    cells = get_next(grid, prev, cur)

    if cells:
      # cell: (new_prev, new_cur) where new_prev is old cur
      for cell in cells:
        if tuple(cell) not in visited:
          q.append(cell)

    # print(q)
  for line in grid2:
    print("".join(line))
  # print(energized)
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
  print(main(test3, test3))
  # print(len(lines))
  # print(len(lines[0]))