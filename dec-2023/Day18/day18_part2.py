# This solution uses the Shoelace formula to calculate the area of the polygon from the vertices
# It then uses Pick's theorem to count the number of interior points, and adds to this the perimeter
# to get the whole shape

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

hex_to_dir = {
  "0" : "R",
  "1" : "D",
  "2" : "L",
  "3" : "U"
}

dirs = {
  "U" : (-1, 0),
  "D" : (1, 0),
  "L" : (0, -1),
  "R" : (0, 1)
}


def main(lst):
  inst = get_instructions(lst)
  vertices = get_vertices(inst)
  area = get_area(vertices) # Shoelace formula
  return area - (get_perimeter(inst)/2) + 1 + get_perimeter(inst) # Pick's formula + perimeter


def get_instructions(lst):
  res = []
  for d, n, h in lst:
    res.append([int(h[1:-1], 16), hex_to_dir[h[-1]]])
  return res


def get_vertices(lst):
  res = [(0, 0)]
  cur = (0, 0)

  for n, d in lst:
    dir = dirs[d]
    r, c = cur
    dr, dc = dir
    dr *= n
    dc *= n

    coord = (r + dr, c + dc)
    res.append(coord)
    cur = coord
  return res[:-1]


def get_area(coords):
  # Shoelace Formula: A = 1/2|(x1y2 + x2y3 + ... + xny1) - (y1x2 + y2x3 + ... + ynx1)|
  part1 = 0
  part2 = 0

  for i in range(len(coords) - 1):
    x1 = coords[i][0]
    y1 = coords[i][1]
    x2 = coords[i + 1][0]
    y2 = coords[i + 1][1]

    part1 += x1 * y2
    part2 += y1 * x2

  xn = coords[-1][0]
  yn = coords[-1][1]
  x1 = coords[0][0]
  y1 = coords[0][1]

  part1 += xn * y1
  part2 += yn * x1

  return .5 * abs(part1 - part2)


def get_perimeter(vertices):
  res = 0
  for n, d in vertices:
    res += n
  return res



if __name__ == "__main__":
  print(main(lines))