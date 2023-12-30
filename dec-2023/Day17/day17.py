with open('Day17/data.txt', 'r') as file:
  lines = file.readlines()
lines = [[int(char) for char in list(line.strip())] for line in lines]


with open('Day17/test.txt', 'r') as file:
  test = file.readlines()
test = [[int(char) for char in list(line.strip())] for line in test]

with open('Day17/test2.txt', 'r') as file:
  test2 = file.readlines()
test2 = [[int(char) for char in list(line.strip())] for line in test2]

dirs = {
  "N" : (-1, 0),
  "S" : (1, 0),
  "E" : (0, 1),
  "W" : (0, -1)
}


def main(grid):
  ROWS = len(grid)
  COLS = len(grid[0])
  res = [float("inf")]

  def dfs(r, c, s, d, weight, visited): # row, col, step_count, direction, weight, visited
    if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited:
      return
    
    if r == ROWS - 1 and c == COLS - 1:
      res[0] = min(res[0], weight)
      return

    new_visited = visited.copy()
    new_visited.add((r, c))

    for dir in dirs.keys():
      if d != dir:
        dfs(r + dirs[dir][0], c + dirs[dir][1], 1, dir, weight + grid[r][c], new_visited)

      if d == dir and s < 3:
        dfs(r + dirs[dir][0], c + dirs[dir][1], s + 1, dir, weight + grid[r][c], new_visited)
  
    return

  dfs(0, 1, 1, "E", 0, set())
  dfs(1, 0, 1, "S", 0, set())
  return res[0]


if __name__ == "__main__":
  print(main(test2))
  