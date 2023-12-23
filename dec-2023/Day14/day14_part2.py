test = [
  'O....#....',
  'O.OO#....#',
  '.....##...',
  'OO.#O....O',
  '.O.....O#.',
  'O.#..O.#.#',
  '..O..#O..O',
  '.......O..',
  '#....###..',
  '#OO..#....'
  ]

[
['.', '.', '.', '.', '.', '#', '.', '.', '.', '.'], 
['.', '.', '.', '.', '#', '.', '.', '.', 'O', '#'], 
['.', '.', '.', '.', '.', '#', '#', '.', '.', '.'], 
['.', '.', 'O', '#', '.', '.', '.', '.', '.', '.'], 
['.', '.', '.', '.', '.', 'O', 'O', 'O', '#', '.'], 
['.', 'O', '#', '.', '.', '.', 'O', '#', '.', '#'], 
['.', '.', '.', '.', 'O', '#', '.', '.', '.', 'O'], 
['.', '.', '.', '.', '.', '.', '.', 'O', 'O', 'O'], 
['#', '.', '.', '.', 'O', '#', '#', '#', '.', 'O'], 
['#', '.', 'O', 'O', 'O', '#', '.', '.', '.', 'O']]




with open('Day14/data.txt', 'r') as file:
  lines = file.readlines()
lines = [line.strip() for line in lines]


def main(grid, num_cycles):
  new_grid = run_cycles(grid, num_cycles)
  return count_weighted_rows(new_grid)


def run_cycles(grid, num_cycles):
  cur_grid = grid
  cache = {}
  for n in range(num_cycles):
    cur_grid = spin(cur_grid, cache)
  return cur_grid


def spin(grid, cache):
  str_grid = stringify(grid)
  if str_grid in cache:
    return gridify(cache[str_grid])
  
  hashed = get_hash(grid, "North")
  cur_grid = get_north_grid(grid, hashed)
  # print(f'north grid: {cur_grid}')
  hashed = get_hash(cur_grid, "West")
  cur_grid = get_west_grid(grid, hashed)
  # print(f'west grid: {cur_grid}')
  hashed = get_hash(cur_grid, "South")
  cur_grid = get_south_grid(grid, hashed)
  # print(f'south grid: {cur_grid}')
  hashed = get_hash(cur_grid, "East")
  cur_grid = get_east_grid(grid, hashed)
  # print(f'east grid: {cur_grid}') 

  cache[str_grid] = stringify(cur_grid)
  return cur_grid


def get_hash(grid, dir):
  if dir == "North":
    return hash_cols(grid, 0, len(grid), 1)
  elif dir == "South":
    return hash_cols(grid, len(grid) - 1, -1, -1)
  elif dir == "East":
    return hash_rows(grid, len(grid[0]) - 1, -1, -1)
  elif dir == "West":
    return hash_rows(grid, 0, len(grid[0]), 1)
  else:
    return None


def hash_cols(grid, row_start, row_end, row_step):
  COLS = len(grid[0])
  
  cols = {} # c : [(O count, # row index)...]
  
  for c in range(COLS):
    cols[c] = []
    o_count = 0
    for r in range(row_start, row_end, row_step):
      if grid[r][c] == "O":
        o_count += 1
      if grid[r][c] == "#":
        cols[c].append((o_count, r))
        o_count = 0
    if o_count > 0:
      cols[c].append((o_count, -1))
  return cols


def hash_rows(grid, col_start, col_end, col_step):
  ROWS = len(grid)
  COLS = len(grid[0])
  
  rows = {} # c : [(O count, # row index)...]
  
  for r in range(ROWS):
    rows[r] = []
    o_count = 0
    for c in range(col_start, col_end, col_step):
      if grid[r][c] == "O":
        o_count += 1
      if grid[r][c] == "#":
        rows[r].append((o_count, c))
        o_count = 0
    if o_count > 0:
      rows[r].append((o_count, -1))
  return rows
  


def get_north_grid(grid, grid_map):
  ROWS = len(grid)
  COLS = len(grid[0])
  new_grid = [["." for _ in range(COLS)] for _ in range(ROWS)]

  for c, vals in grid_map.items():
    last_pound = 0
    for o_count, pound_idx in vals:
      for r in range(o_count):
        new_grid[last_pound + r][c] = "O"
      if pound_idx != -1:
        new_grid[pound_idx][c] = "#"
        last_pound = pound_idx + 1
  return new_grid

def get_south_grid(grid, grid_map):
  ROWS = len(grid)
  COLS = len(grid[0])
  new_grid = [["." for _ in range(COLS)] for _ in range(ROWS)]

  for c, vals in grid_map.items():
    last_pound = COLS - 1
    for o_count, pound_idx in vals:
      for r in range(o_count):
        new_grid[last_pound - r][c] = "O"
      if pound_idx != -1:
        new_grid[pound_idx][c] = "#"
        last_pound = pound_idx - 1
  return new_grid

def get_west_grid(grid, grid_map):
  ROWS = len(grid)
  COLS = len(grid[0])
  new_grid = [["." for _ in range(COLS)] for _ in range(ROWS)]

  for r, vals in grid_map.items():
    last_pound = 0
    for o_count, pound_idx in vals:
      for c in range(o_count):
        new_grid[r][last_pound + c] = "O"
      if pound_idx != -1:
        new_grid[r][pound_idx] = "#"
        last_pound = pound_idx + 1
  return new_grid



def get_east_grid(grid, grid_map):
  ROWS = len(grid)
  COLS = len(grid[0])
  new_grid = [["." for _ in range(COLS)] for _ in range(ROWS)]

  for r, vals in grid_map.items():
    last_pound = ROWS - 1
    for o_count, pound_idx in vals:
      for c in range(o_count):
        new_grid[r][last_pound - c] = "O"
      if pound_idx != -1:
        new_grid[r][pound_idx] = "#"
        last_pound = pound_idx - 1
  return new_grid


def stringify(grid):
  ROWS = len(grid)
  COLS = len(grid[0])

  res = ""

  for r in range(ROWS):
    for c in range(COLS):
      res += grid[r][c]
    res += ';'
  return res

def gridify(str):
  return str.split(';')[:-1]

def count_weighted_rows(grid):
  ROWS = len(grid)
  COLS = len(grid[0])
  factor = len(grid) + 1
  res = 0

  for r in range(ROWS):
    factor -= 1
    for c in range(COLS):
      if grid[r][c] == "O":
        res += factor
  
  return res


if __name__ == "__main__":
  print(main(lines, 1000))
  # print(lines)
