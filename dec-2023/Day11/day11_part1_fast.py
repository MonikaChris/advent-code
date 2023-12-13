# Fast Part 1 Solution using coordinate math

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


def main(uni):
  galaxy_count = sub_nums(uni) # Sub numbers for # in input
  expand_uni(uni)
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


def expand_uni(uni):
    ROWS = len(uni)
    COLS = len(uni[0])

    # Expand rows
    r = 0
    while r < ROWS:
      for c in range(COLS):
        if uni[r][c] != '.':
            break
        if c == COLS - 1:
            new_row = ['.'] * COLS
            uni.insert(r + 1, new_row)
            r += 1
            ROWS += 1  
      r += 1

    # Expand cols
    c = 0
    while c < COLS:
      for r in range(ROWS):
        if uni[r][c] != '.':
            break
        if r == ROWS - 1:
            for i in range(ROWS):
                uni[i].insert(c + 1, '.')
            c += 1
            COLS += 1  
      c += 1
    return uni


def get_galaxy_coords(uni, galaxy_count):
  ROWS = len(uni)
  COLS = len(uni[0])

  coords = [0] * (galaxy_count + 1)

  for r in range(ROWS):
    for c in range(COLS):
      if uni[r][c] != '.':
        coords[int(uni[r][c])] = (r, c)
  return coords


def get_paths_sum(start, end, coords, uni):
  # Returns sum of shortest paths from starting galaxy i to all galaxies below it
  ROWS = len(uni)
  COLS = len(uni[0])
  paths = []

  for i in range(start + 1, end + 1):
    paths.append(get_path(start, i, coords, uni))
  return sum(paths)


def get_path(start, end, coords, uni):
  sr = coords[start][0]
  sc = coords[start][1]
  er = coords[end][0]
  ec = coords[end][1]

  return abs(sr - er) + abs(sc - ec)
  
  

if __name__ == "__main__":
  print(main(universe))
  