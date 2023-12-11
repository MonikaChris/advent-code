test_grid = [
  ['.', '.', 'F', '7', '.'],
  ['.', 'F', 'J', '|', '.'],
  ['S', 'J', '.', 'L', '7'],
  ['|', 'F', '-', '-', 'J'],
  ['L', 'J', '.', '.', '.']
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
  s = getStart(grid)
  steps = countSteps(s, grid)
  return (steps + 1)//2


def getStart(grid):
  ROWS = len(grid)
  COLS = len(grid[0])

  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == 'S':
        return [r, c]
  return -1


def countSteps(s, grid):
  next = getFirstStep(s, grid)
  prev = [s[0], s[1]]
  r = next[0]
  c = next[1]
  step_count = 1

  while [r, c] != s:
    cell1, cell2 = pipes[grid[r][c]]
    if [r + cell1[0], c + cell1[1]] != prev:
      prev = [r, c]
      r = cell1[0] + r
      c = cell1[1] + c
    else:
      prev = [r, c]
      r = cell2[0] + r
      c = cell2[1] + c
    step_count += 1
  return step_count
    

def getFirstStep(s, grid):
  r = s[0]
  c = s[1]
  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  for dr, dc in directions:
    # Adjacent square has pipe and pipe is properly oriented
    if grid[r + dr][c + dc] in pipes and pipes[grid[r + dr][c + dc]][0] == [-1 * dr, -1 * dc] or pipes[grid[r + dr][c + dc]][1] == [-1 * dr, -1 * dc]:
      return [r + dr, c + dc]
  return -1




if __name__ == "__main__":
  print(main(lines))  