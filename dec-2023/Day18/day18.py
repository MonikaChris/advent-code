with open('Day18/data.txt', 'r') as file:
  lines = file.readlines()

with open('Day18/test.txt', 'r') as file:
  test = file.readlines()


def format_data(data):
  info = []
  for line in data:
    parts = line.strip().split()
    parts[1] = int(parts[1])
    parts[2] = parts[2][1:-1]
    info.append(parts)
  return info

lines = format_data(lines)
test = format_data(test)

dirs = {
  "U" : (-1, 0),
  "D" : (1, 0),
  "L" : (0, -1),
  "R" : (0, 1)
}


def main(lst):
  grid = mark_path(lst)
  grid = flood(grid)
  new_grid = ["".join(line) for line in grid]
  return count_area(grid)


def get_dimensions(lst):
  # Returns max vertical and horizontal dimensions
  rows = 0
  cols = 0

  # Handles offset when changing directions
  row_count = 0
  col_count = 0
  
  for dir, val, color in lst:
    if dir == "U" or dir == "D":
      rows += val
      row_count += 1
    else:
      cols += val
      col_count += 1
  return rows + col_count, cols + row_count


def mark_path(lst):
  rows, cols = get_dimensions(lst)
  grid = [['.'] * (cols + 1) for _ in range(rows + 1)]
  start_r = (rows + 1) // 2
  start_c = (cols + 1) // 2

  r = start_r
  c = start_c

  grid[r][c] = "#"
  for d, n, color in lst:
    for _ in range(n):
      grid[r][c] = "#"
      r += dirs[d][0]
      c += dirs[d][1]

  return grid


def flood(grid):
  ROWS = len(grid)
  COLS = len(grid[0])
  visited = set()

  for r in range(ROWS):
    dfs(grid, r, 0, visited)

  for r in range(ROWS):
    dfs(grid, r, COLS - 1, visited)

  for c in range(COLS):
    dfs(grid, 0, c, visited)
  
  for c in range(COLS):
    dfs(grid, ROWS - 1, c, visited)

  return grid


def dfs(grid, r, c, visited):
  ROWS = len(grid)
  COLS = len(grid[0])

  if (r < 0 or r >= ROWS or
      c < 0 or c >= COLS or
      (r, c) in visited or
      grid[r][c] != '.'):
      return

  grid[r][c] = "O"
  
  for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    dr, dc = r + d[0], c + d[1]
    dfs(grid, dr, dc, visited)

  return grid


def count_area(grid):
  ROWS = len(grid)
  COLS = len(grid[0])

  res = 0

  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] != "O":
        res += 1

  return res
    


if __name__ == "__main__":
  print(main(lines))
  
