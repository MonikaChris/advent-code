# This is a first attempt that fails because "there doesn't even need to be a full tile path 
# to the outside for tiles to count as outside the loop - squeezing between pipes is also allowed"
# This approach finds the tiles connected to the outside, so it misses these edge cases.


test_grid = [
  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
  ['.', 'S', '-', '-', '-','-', '-', '-', '-', '7', '.'],
  ['.', '|', 'F', '-', '-', '-', '-', '-', '7', '|', '.'],
  ['.', '|', '|', '.', '.', '.', '.', '.', '|', '|', '.'],
  ['.', '|', '|', '.', '.', '.', '.', '.', '|', '|', '.'],
  ['.', '|', 'L', '-', '7', '.', 'F', '-', 'J', '|', '.'],
  ['.', '|', '.', '.', '|', '.', '|', '.', '.', '|', '.'],
  ['.', 'L', '-', '-', 'J', '.', 'L', '-', '-', 'J', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]

test_grid2 = [
  ['.', 'F', '-', '-', '-', '-', '7', 'F', '7', 'F', '7', 'F', '7', 'F', '-', '7', '.', '.', '.', '.'], 
  ['.', '|', 'F', '-', '-', '7', '|', '|', '|', '|', '|', '|', '|', '|', 'F', 'J', '.', '.', '.', '.'], 
  ['.', '|', '|', '.', 'F', 'J', '|', '|', '|', '|', '|', '|', '|', '|', 'L', '7', '.', '.', '.', '.'], 
  ['F', 'J', 'L', '7', 'L', '7', 'L', 'J', 'L', 'J', '|', '|', 'L', 'J', '.', 'L', '-', '7', '.', '.'], 
  ['L', '-', '-', 'J', '.', 'L', '7', '.', '.', '.', 'L', 'J', 'S', '7', 'F', '-', '7', 'L', '7', '.'], 
  ['.', '.', '.', '.', 'F', '-', 'J', '.', '.', 'F', '7', 'F', 'J', '|', 'L', '7', 'L', '7', 'L', '7'], 
  ['.', '.', '.', '.', 'L', '7', '.', 'F', '7', '|', '|', 'L', '7', '|', '.', 'L', '7', 'L', '7', '|'], 
  ['.', '.', '.', '.', '.', '|', 'F', 'J', 'L', 'J', '|', 'F', 'J', '|', 'F', '7', '|', '.', 'L', 'J'], 
  ['.', '.', '.', '.', 'F', 'J', 'L', '-', '7', '.', '|', '|', '.', '|', '|', '|', '|', '.', '.', '.'], 
  ['.', '.', '.', '.', 'L', '-', '-', '-', 'J', '.', 'L', 'J', '.', 'L', 'J', 'L', 'J', '.', '.', '.']
  ]

  
test_grid3 = [
  ['F', 'F', '7', 'F', 'S', 'F', '7', 'F', '7', 'F', '7', 'F', '7', 'F', '7', 'F', '-', '-', '-', '7'], 
  ['L', '|', 'L', 'J', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', 'F', '-', '-', 'J'], 
  ['F', 'L', '-', '7', 'L', 'J', 'L', 'J', '|', '|', '|', '|', '|', '|', 'L', 'J', 'L', '-', '7', '7'], 
  ['F', '-', '-', 'J', 'F', '-', '-', '7', '|', '|', 'L', 'J', 'L', 'J', 'I', 'F', '7', 'F', 'J', '-'], 
  ['L', '-', '-', '-', 'J', 'F', '-', 'J', 'L', 'J', 'I', 'I', 'I', 'I', 'F', 'J', 'L', 'J', 'J', '7'], 
  ['|', 'F', '|', 'F', '-', 'J', 'F', '-', '-', '-', '7', 'I', 'I', 'I', 'L', '7', 'L', '|', '7', '|'], 
  ['|', 'F', 'F', 'J', 'F', '7', 'L', '7', 'F', '-', 'J', 'F', '7', 'I', 'I', 'L', '-', '-', '-', '7'], 
  ['7', '-', 'L', '-', 'J', 'L', '7', '|', '|', 'F', '7', '|', 'L', '7', 'F', '-', '7', 'F', '7', '|'], 
  ['L', '.', 'L', '7', 'L', 'F', 'J', '|', '|', '|', '|', '|', 'F', 'J', 'L', '7', '|', '|', 'L', 'J'], 
  ['L', '7', 'J', 'L', 'J', 'L', '-', 'J', 'L', 'J', 'L', 'J', 'L', '-', '-', 'J', 'L', 'J', '.', 'L']
  ]


with open('Day10/data.txt', 'r') as file:
  lines = file.readlines()
# lines = [line.strip().split('\n') for line in lines]
lines = [list(line.strip()) for line in lines]

pipes = {
  "|" : ([1, 0], [-1, 0]),
  '-' : ([0, -1], [0, 1]),
  'L' : ([-1, 0], [0, 1]),
  'J' : ([0, -1], [-1, 0]),
  '7' : ([0, -1], [1, 0]),
  'F' : ([1, 0], [0, 1])
}


def main(grid):
  s = get_start(grid)
  mark_path(s, grid)
  mark_surroundings(grid)
  return get_enclosed_area(grid)


def get_start(grid):
  ROWS = len(grid)
  COLS = len(grid[0])

  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == 'S':
        return [r, c]
  return -1


def mark_path(s, grid):
  next = get_first_step(s, grid)
  prev = [s[0], s[1]]
  r = next[0]
  c = next[1]

  grid[s[0]][s[1]] = "P"
  
  while [r, c] != s:
    cell1, cell2 = pipes[grid[r][c]]
    grid[r][c] = "P"
    if [r + cell1[0], c + cell1[1]] != prev:
      prev = [r, c]
      r = cell1[0] + r
      c = cell1[1] + c
    else:
      prev = [r, c]
      r = cell2[0] + r
      c = cell2[1] + c
    # grid[r][c] = 'P'
  return grid
    

def get_first_step(s, grid):
  r = s[0]
  c = s[1]
  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  for dr, dc in directions:
    # Adjacent square has pipe and pipe is properly oriented
    if grid[r + dr][c + dc] in pipes and pipes[grid[r + dr][c + dc]][0] == [-1 * dr, -1 * dc] or pipes[grid[r + dr][c + dc]][1] == [-1 * dr, -1 * dc]:
      return [r + dr, c + dc]
  return -1

def mark_surroundings(grid):
  ROWS = len(grid)
  COLS = len(grid[0])
  visited = set()
  stack = []
  
  for r in range(ROWS):
    stack.append((r, 0))
    stack.append((r, COLS - 1))

  for c in range(COLS):
    stack.append((0, c))
    stack.append((ROWS - 1, c))

  while stack:
    r, c = stack.pop()
    if (r < 0 or r >= ROWS or
      c < 0 or c >= COLS or
      (r, c) in visited or
      grid[r][c] == "P"):
      continue

    grid[r][c] = "S"
    visited.add((r, c))

    stack.append((r + 1, c))
    stack.append((r - 1, c))
    stack.append((r, c + 1))
    stack.append((r, c - 1))
    # Diagonals
    # stack.append((r - 1, c - 1))
    # stack.append((r + 1, c - 1))
    # stack.append((r - 1, c + 1))
    # stack.append((r + 1, c + 1))
  return grid


def get_enclosed_area(grid):
  ROWS = len(grid)
  COLS = len(grid[0])

  area = 0

  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] != 'P' and grid[r][c] != 'S':
        area += 1
  return area



if __name__ == "__main__":
  print(main(test_grid2))
  # new_grid = mark_path([4, 12], test_grid2)
  # print(mark_surroundings(new_grid))
