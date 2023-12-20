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

with open('Day14/data.txt', 'r') as file:
  lines = file.readlines()
lines = [line.strip() for line in lines]


def main(grid):
  new_grid = shift_north(grid)
  return count_weighted_rows(new_grid)


def shift_north(grid):
  ROWS = len(grid)
  COLS = len(grid[0])
  
  cols = {} # c : [(O count, # row index)...]
  
  for c in range(COLS):
    cols[c] = []
    o_count = 0
    for r in range(ROWS):
      if grid[r][c] == "O":
        o_count += 1
      if grid[r][c] == "#":
        cols[c].append((o_count, r))
        o_count = 0
    if o_count > 0:
      cols[c].append((o_count, -1))
  
  return make_north_grid(grid, cols)


def make_north_grid(grid, cols):
  ROWS = len(grid)
  COLS = len(grid[0])

  new_grid = [["." for _ in range(COLS)] for _ in range(ROWS)]

  for c, vals in cols.items():
    last_hash = 0
    for o_count, hash_idx in vals:
      for r in range(o_count):
        new_grid[last_hash + r][c] = "O"
      if hash_idx != -1:
        new_grid[hash_idx][c] = "#"
        last_hash = hash_idx + 1

  # Output new_grid to file to confirm visually
  write_grid_to_file(new_grid, 'Day14/output.txt')
  return new_grid


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


def write_grid_to_file(grid, filename):
  # Troubleshooting function to confirm new grid output
  with open(filename, 'w') as file:
    for sublist in grid:
      file.write(str(sublist) + '\n')


def count_symbols(grid):
  # Troubleshooting function to confirm new grid output
  ROWS = len(grid)
  COLS = len(grid[0])

  hash_count = 0
  o_count = 0
  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == "O":
        o_count += 1
      if grid[r][c] == "#":
        hash_count += 1
  
  print(f'#: {hash_count} O: {o_count}')



if __name__ == "__main__":
  print(main(lines))
  # new_grid = shift_north(lines)
  # count_symbols(lines)
  # count_symbols(new_grid)


  