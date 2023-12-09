import math

# Test Data
test_dir = 'LR'
test_graph = {
  '11A' : ('11B', 'XXX'),
  '11B' : ('XXX', '11Z'),
  '11Z' : ('11B', 'XXX'),
  '22A' : ('22B', 'XXX'),
  '22B' : ('22C', '22C'),
  '22C' : ('22Z', '22Z'),
  '22Z' : ('22B', '22B'),
  'XXX' : ('XXX', 'XXX')
}

# Real Data
with open('Day8/data.txt', 'r') as file:
  lines = file.readlines()

directions = lines[0].strip()
remaining_lines = [line.strip() for line in lines[1:] if line.strip()] #Removes empty strings

graph = {}
for line in remaining_lines:
  if '=' in line:
    key, value = line.split('=')
    key = key.strip()
    value = tuple(val.strip() for val in value.strip()[1:-1].split(','))
    graph[key] = value


DIR = {
  'L' : 0,
  'R' : 1
}

def main(directions, graph):
  nodes = getStartNodes(graph)
  steps = []
  for node in nodes:
    steps.append(getSteps(directions, graph, node))
  return lcm(steps)


def lcm(nums):
  def lcm_of_two_nums(a, b):
    return a * b // math.gcd(a, b)
  
  lcm = nums[0]
  for i in range(1, len(nums)):
    lcm = lcm_of_two_nums(lcm, nums[i])
  return lcm
  

def getSteps(directions, graph, start):
  cur = start
  i = 0
  steps = 0

  while cur[-1] != 'Z':
    cur = graph[cur][DIR[directions[i]]]  # Gets index 0 or index 1 from graph tuple based on current direction
    steps += 1
    i = (i + 1) % len(directions)
  return steps


def getStartNodes(graph):
  res = []
  for node in graph.keys():
    if node[-1] == "A":
      res.append(node)
  return res


def bruteForce(directions, graph):
  nodes = getStartNodes(graph)
  i = 0
  steps = 0
  run = True

  while run:
    for n, node in enumerate(nodes):
      nodes[n] = graph[node][DIR[directions[i]]]  # Gets index 0 or index 1 from graph tuple based on current direction
    steps += 1
    for node in nodes:
      run = False
      if node[-1] != 'Z':
       run = True
       break
    i = (i + 1) % len(directions)
  return steps



if __name__ == "__main__":
  # print(main(test_dir, test_graph))
  print(main(directions, graph))
