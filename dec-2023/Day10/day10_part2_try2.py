

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
  path = get_path_coords(s, grid)
  area = get_path_area(path)
  return (area - (len(path)/2) + 1)


def get_start(grid):
  ROWS = len(grid)
  COLS = len(grid[0])

  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == 'S':
        return [r, c]
  return -1


def get_path_coords(s, grid):
  next = get_first_step(s, grid)
  prev = [s[0], s[1]]
  r = next[0]
  c = next[1]

  path_coords = [next]

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
    path_coords.append([r, c])
  return path_coords
    

def get_first_step(s, grid):
  r = s[0]
  c = s[1]
  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  for dr, dc in directions:
    # Adjacent square has pipe and pipe is properly oriented
    if grid[r + dr][c + dc] in pipes and pipes[grid[r + dr][c + dc]][0] == [-1 * dr, -1 * dc] or pipes[grid[r + dr][c + dc]][1] == [-1 * dr, -1 * dc]:
      return [r + dr, c + dc]
  return -1


def get_path_area(coords):
  # A = 1/2|(x1y2 + x2y3 + ... + xny1) - (y1x2 + y2x3 + ... + ynx1)|
  half1 = 0
  half2 = 0
  for i in range(len(coords) - 1):
    half1 += coords[i][0] * coords[i + 1][1]
    half2 += coords[i][1] * coords[i + 1][0]
  
  half1 += coords[-1][0] * coords[0][1]
  half2 += coords[-1][1] * coords[0][0]

  return .5 * abs(half1 - half2)



if __name__ == "__main__":
  print(main(lines))
  # coords = get_path_coords([1, 1], test_grid)
  # print(get_path_area(coords))
