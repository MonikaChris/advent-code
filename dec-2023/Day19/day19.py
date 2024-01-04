with open('Day19/data.txt', 'r') as file:
  lines = file.readlines()

with open('Day19/test.txt', 'r') as file:
  test = file.readlines()

def format(data):
  index = data.index("\n")
  workflows = data[:index]
  parts = data[index + 1:]

  workflows = [line.strip() for line in workflows]
  parts = [line.strip() for line in parts]
  
  return workflows, parts

workflows, parts = format(lines)
test_flows, test_parts = format(test)



def main(flows, parts):
  flow_map = get_flow_map(flows)
  res = 0
  for part in parts:
    res += process(part, flow_map)
  return res


def get_flow_map(flows):
  map = {}
  for flow in flows:
    key, val = flow.split("{", 1)
    val = val[:-1]
    val = val.split(",")
    map[key] = val
  return map


def process(part, flow_map):
  part, x, m, a, s = make_dict(part)
  next = "in"
  while next != "R" and next != "A":
    next = run(flow_map[next], part)
    
  return x + m + a + s if next == "A" else 0


def run(flow_map, part):
  for map in flow_map:
    if ':' not in map:
      return map
    else:
      rule, dest = map.split(':')
      char = rule[0]
      symbol = rule[1]
      num = int(rule[2:])

      if symbol == ">":
        if part[char] > num:
          return dest
        else:
          continue

      elif symbol == "<":
        if part[char] < num:
          return dest
        else:
          continue


def make_dict(part):
  # {x=787,m=2655,a=1222,s=2876}
  part = part[1:-1]
  x, m, a, s = part.split(',')
  part_dict = {'x': int(x[2:]), 'm': int(m[2:]), 'a': int(a[2:]), 's': int(s[2:])}
  return part_dict, int(x[2:]), int(m[2:]), int(a[2:]), int(s[2:])

if __name__ == "__main__":
  print(main(workflows, parts))