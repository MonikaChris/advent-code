with open('Day3/data.txt', 'r') as file:
  lines = file.readlines()
grid = [line.strip() for line in lines]

#Testing - remove
# grid = [
#   "....401.............425.......323......791......697...............963............................................420........................",
#   "...*..................................%......#.....*....290.........................492.............656...@953.....................+830.....",
#   "..159...........823...33.717.....572.......806...896......-.....335....834......815.............791....*..............776...................",
#   ".........-.....#........*.........*..................715..........*.....*........*.....................5...*.....................688........"
#   ]

# grid = [
#   "467..114..",
#   "...*......",
#   "..35..633.",
#   "......#...",
#   "617*......",
#   ".....+.58.",
#   "..592.....",
#   "......755.",
#   "...$.*....",
#   ".664.598.."
#   ]

ROWS = len(grid)
COLS = len(grid[0])
SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '/']

visited = set()

# Main function for part 2
def getGearNum(grid):
  res = 0
  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] in SYMBOLS:
        nums = getAdjNums(r,c)
        if len(nums) == 2:
          res += nums[0] * nums[1]
  return res

# Main function for part 1
def getPartNums(grid):
  res = 0
  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] in SYMBOLS:
        nums = getAdjNums(r, c)
        for num in nums:
          res += num
  return res

def getAdjNums(r,c):
  res = []
  # Check all directions around symbols for digits
  directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),(1, 1)]
  for dr, dc in directions:
    if ((dr + r) >= 0 and (dr + r) < ROWS and
        (dc + c) >= 0 and (dc + c) < COLS and
        isNum(grid[dr + r][dc + c]) and 
        (dr + r, dc + c) not in visited):
      #Get coordinates of all local contiguous digits
      coords = getCoords(dr + r, dc + c)
      #Convert coordinates to correctly ordered digits
      res.append(processCords(coords))
  return res

def getCoords(r, c):
  res = []
  def dfs(r,c):
    if (r < 0 or r >= ROWS or
      c < 0 or c >= COLS or
      (r, c) in visited or
      not isNum(grid[r][c])):
      return
    visited.add((r,c))
    res.append((r,c))
    dfs(r, c + 1)
    dfs(r, c-1)
  dfs(r, c)
  return res

def processCords(coords):
  coords.sort(key=lambda x: x[1])
  res = ""
  for r, c in coords:
    res += grid[r][c]
  return int(res)


def isNum(char):
  return (ord("0") <= ord(char) <= ord("9"))




if __name__ == "__main__":
  # total = getPartNums(grid)
  # print(total)

  total2 = getGearNum(grid)
  print(total2)
  
  # total2 = getPartNums(grid)
  # print(total2)