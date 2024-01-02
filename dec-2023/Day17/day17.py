import heapq

with open('Day17/data.txt', 'r') as file:
  lines = file.readlines()
lines = [[int(char) for char in list(line.strip())] for line in lines]


with open('Day17/test.txt', 'r') as file:
  test = file.readlines()
test = [[int(char) for char in list(line.strip())] for line in test]

dirs = {
  "N" : (-1, 0),
  "S" : (1, 0),
  "E" : (0, 1),
  "W" : (0, -1)
}

opp = {
  "N" : "S",
  "S" : "N",
  "E" : "W",
  "W" : "E"
}

def main(grid):
  ROWS = len(grid)
  COLS = len(grid[0])
  pq = [] #(cost, (r, c, d, s)) - row, col, direction, step
  heapq.heappush(pq, (grid[0][1], (0, 1, "E", 1)))
  heapq.heappush(pq, (grid[1][0], (1, 0, "S", 1)))
  cost = {}
  cost[(0, 1, "E", 1)] = grid[0][1]
  cost[(1, 0, "S", 1)] = grid[1][0]
  path = {}
  path[(0, 1, "E", 1)] = None
  path[(1, 0, "S", 1)] = None

  while pq:
    cur_cost, (r, c, d, s) = heapq.heappop(pq)

    if r == ROWS - 1 and c == COLS - 1:
      # Check path - for troubleshooting
      # cur = path[(r, c, d, s)]
      # cur_path = []
      # while cur:
      #   cur_path.append(cur)
      #   cur = path[cur]
      # cur_path.reverse()
      # print(cur_path)
      return cur_cost

    for dir in dirs:
      dr, dc = r + dirs[dir][0], c + dirs[dir][1]

      if 0 <= dr < ROWS and 0 <= dc < COLS:
        new_cost = cur_cost + grid[dr][dc]
        
        # New direction
        if d != dir and dir != opp[d]:
          if (dr, dc, dir, 1) not in cost or cost[(dr, dc, dir, 1)] > new_cost:
            heapq.heappush(pq, (new_cost, (dr, dc, dir, 1)))
            cost[(dr, dc, dir, 1)] = new_cost
            path[(dr, dc, dir, 1)] = (r, c, d, s)
    
        # Same direction
        if d == dir and s < 3 and dir != opp[d]:
          if (dr, dc, dir, s + 1) not in cost or cost[(dr, dc, dir, s + 1)] > new_cost:
            heapq.heappush(pq, (new_cost, (dr, dc, dir, s + 1)))
            cost[(dr, dc, dir, s + 1)] = new_cost
            path[(dr, dc, dir, s + 1)] = (r, c, d, s)




if __name__ == "__main__":
  print(main(lines))
