import math

with open('Day6/data.txt', 'r') as file:
  lines = file.readlines()
lines = [line.strip() for line in lines]

# Part 1 data
times1 = [int(num) for num in lines[0].split()[1:]]
dists1 = [int(num) for num in lines[1].split()[1:]]

# Part 2 data
times2 = [int("".join(line for line in lines[0].split()[1:]))]
dists2 = [int("".join(line for line in lines[1].split()[1:]))]

# d = vt
# parameter x
# d = (0 + x)(t - x)
# d = x(t-x)
# Solve: 0 = -x^2 + tx - d
# range: btwn root1 and root2, non-inclusive, round to whole numbers


def main(times, dists):
  res = 1
  for i in range(len(times)):
    a = -1
    b = times[i]
    c = -1 * dists[i]

    root1, root2 = quad_formula(a, b, c)

    root1 = int(root1) + 1 if root1.is_integer() else math.ceil(root1)
    root2 = int(root2) - 1 if root2.is_integer() else math.floor(root2)

    num_ways = root2 - root1 + 1
    res *= num_ways
  return res

def quad_formula(a, b, c):
  disc = b ** 2 - 4 * a * c
  if disc < 0:
    return "No real roots"
  root1 = (-b + math.sqrt(disc)) / (2 * a)
  root2 = (-b - math.sqrt(disc)) / (2 * a)

  # Return smaller root, then larger root
  if root1 > root2:
    root1 = temp
    root2 = root1
    root1 = temp

  return root1, root2



if __name__ == "__main__":
  # Part 1
  print(main(times1, dists1))

  # Part 2
  print(main(times2, dists2))
  
  # print(quad_formula(-1, 15, -40))
  # print(quad_formula(-1, 7, -9))
  # print(quad_formula(-1, 30, -200))

  
  