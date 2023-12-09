# Test Data
test_dir = 'LLR'
test_graph = {
  'AAA' : ('BBB', 'BBB'),
  'BBB' : ('AAA', 'ZZZ'),
  'ZZZ' : ('ZZZ', 'ZZZ')
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
  cur = 'AAA'
  i = 0
  steps = 0

  while cur != 'ZZZ':
    cur = graph[cur][DIR[directions[i]]]  # Gets index 0 or index 1 from graph tuple based on current direction
    steps += 1
    i = (i + 1) % len(directions)
  return steps



if __name__ == "__main__":
  print(main(directions, graph))
