from collections import deque

def main(filename, steps):
  grid = get_grid(filename)
  start = get_start(grid) # start = (r, c)
  return bfs(grid, start, steps)


def get_grid(filename):
  with open(f'Day21/{filename}', 'r') as file:
    lines = file.readlines()
  return [line.strip() for line in lines]


def get_start(grid):
  ROWS, COLS = len(grid), len(grid[0])

  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == 'S':
        return (r, c)


def bfs(grid, start, steps):
  ROWS, COLS = len(grid), len(grid[0])
  q = deque([start])

  while steps > 0:
    for _ in range(len(q)):
      r, c = q.popleft()
      for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dr = r + dir[0]
        dc = c + dir[1]
        if (dr >= 0 and dr < ROWS and
            dc >= 0 and dc < COLS and
            grid[dr][dc] != "#" and
            (dr, dc) not in q):
          q.append((dr, dc))
    steps -= 1
  return len(q)


if __name__ == "__main__":
  print(main('data.txt', 64))