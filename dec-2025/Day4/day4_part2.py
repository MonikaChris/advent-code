with open("Day4/data.txt", "r") as file:
  lines = file.readlines()
data = [list(line.strip()) for line in lines]

sampleData = [
  "..@@.@@@@.",
  "@@@.@.@.@@",
  "@@@@@.@.@@",
  "@.@@@@..@.",
  "@@.@@@@.@@",
  ".@@@@@@@.@",
  ".@.@.@.@@@",
  "@.@@@.@@@@",
  ".@@@@@@@@.",
  "@.@.@@@.@."
]
sampleData = [list(s) for s in sampleData]

def countRolls(grid):
  ROWS, COLS = len(grid), len(grid[0])
  rollCount = 0
  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] != "@":
        continue
      
      dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
      count = 0
      for dir in dirs:
        dr = r + dir[0]
        dc = c + dir[1]

        if (dr >= 0 and dr < ROWS and dc >= 0 and dc < COLS and grid[dr][dc] == "@"):
          count += 1
        if count == 4:
          break
      
      if count < 4:
        rollCount += 1
        grid[r][c] = "x"
  return rollCount

def removeRolls(grid):
  count = 0
  while True:
    removedRollsCount = countRolls(grid)
    count += removedRollsCount
    if removedRollsCount == 0:
      break
  return count


if __name__ == "__main__":
  print(removeRolls(sampleData))
  print(removeRolls(data))
