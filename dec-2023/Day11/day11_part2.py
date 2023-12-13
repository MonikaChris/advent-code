test_uni = [
  ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'], 
  ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'], 
  ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'], 
  ['#', '.', '.', '.', '#', '.', '.', '.', '.', '.']]


with open('Day11/data.txt', 'r') as file:
  lines = file.readlines()
universe = [[char for char in line.strip()] for line in lines]

EXP_COEF = 1000000 #Expansion coefficient


def main(uni):
  galaxy_count = sub_nums(uni) # Sub numbers for # in input
  mark_expansions(uni)
  coords = get_galaxy_coords(uni, galaxy_count)
  res = 0
  for galaxy in range(1, galaxy_count):
    res += get_paths_sum(galaxy, galaxy_count, coords, uni)
  return res


def sub_nums(uni):
  ROWS = len(uni)
  COLS = len(uni[0])
  count = 1

  for r in range(ROWS):
    for c in range(COLS):
      if uni[r][c] == '#':
        uni[r][c] = str(count)
        count += 1
  return count - 1


def mark_expansions(uni):
  # Mark expanding rows and cols with X
  ROWS = len(uni)
  COLS = len(uni[0])

  for r in range(ROWS):
    for c in range(COLS):
      if uni[r][c] != "." and uni[r][c] != "X":
        break
      if c == COLS - 1:
        for i in range(COLS):
          uni[r][i] = "X"

  for c in range(COLS):
    for r in range(ROWS):
      if uni[r][c] != "." and uni[r][c] != "X":
        break
      if r == ROWS - 1:
        for i in range(ROWS):
          uni[i][c] = "X"


def get_galaxy_coords(uni, galaxy_count):
  ROWS = len(uni)
  COLS = len(uni[0])

  coords = [0] * (galaxy_count + 1)

  for r in range(ROWS):
    for c in range(COLS):
      if uni[r][c] != '.' and uni[r][c] != 'X':
        coords[int(uni[r][c])] = (r, c)
  return coords

def get_paths_sum(start, last, coords, uni):
  # Returns sum of shortest paths from starting galaxy i to all galaxies below it
  ROWS = len(uni)
  COLS = len(uni[0])
  paths = []

  for end in range(start + 1, last + 1):
    paths.append(get_path(start, end, coords, uni))
  return sum(paths)

def get_path(start, end, coords, uni):
  sr = coords[start][0]
  sc = coords[start][1]
  er = coords[end][0]
  ec = coords[end][1]

  path = abs(sr - er) + abs(sc - ec)

  for r in range(sr + 1, er):
    if uni[r][sc] == "X":
      path += EXP_COEF - 1

  col_start = min(sc, ec)
  col_end = max(sc, ec)

  for c in range(col_start + 1, col_end):
    if uni[er][c] == "X":
      path += EXP_COEF - 1
  
  return path

if __name__ == "__main__":
  print(main(universe))