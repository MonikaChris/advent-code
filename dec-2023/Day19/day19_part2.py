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


def main(workflows):
  flow_map = get_flow_map(workflows)
  flows = get_all_flows(flow_map)
  intervals = merge_intervals(flows)
  return compute_total(intervals)


def get_flow_map(flows):
  map = {}
  for flow in flows:
    key, val = flow.split("{", 1)
    val = val[:-1]
    val = val.split(",")
    map[key] = val
  return map


def get_all_flows(maps):
  res = []
  
  def dfs(maps, next, i, cur_path):
    #Finds all x, m, a, s ranges that lead to A
    
    if next not in maps:
      if next == "A":
        res.append(cur_path.copy())
        return
      if next == "R":
        return

    if ':' not in maps[next][i]:
      dfs(maps, maps[next][i], 0, cur_path.copy())

    else:
      rule, dest = maps[next][i].split(':')
      char = rule[0]
      symbol = rule[1]
      num = rule[2:]

      if symbol == ">":
        cur_path.append(rule)
        dfs(maps, dest, 0, cur_path.copy())
        cur_path.pop(-1)
        cur_path.append(char + "<=" + num)
        dfs(maps, next, i + 1, cur_path.copy())
        

      if symbol == "<":
        cur_path.append(rule)
        dfs(maps, dest, 0, cur_path.copy())
        cur_path.pop(-1)
        cur_path.append(char + ">=" + num)
        dfs(maps, next, i + 1, cur_path.copy())

  dfs(maps, "in", 0, [])
  return res


def merge_intervals(flows):
  [flow.sort() for flow in flows]
  res = []
  for flow in flows:
    chars = {
      "x" : [1, 4000],
      "m" : [1, 4000],
      "a" : [1, 4000],
      "s" : [1, 4000]
    }
    for interval in flow:
      char = interval[0]
      sym = interval[1] if interval[2] != "=" else interval[1:3]
      num = int(interval[2:]) if interval[2] != "=" else int(interval[3:])

      if sym == ">":
        chars[char][0] = max(chars[char][0], num + 1)

      if sym == "<":
        chars[char][1] = min(chars[char][1], num - 1)

      if sym == ">=":
        chars[char][0] = max(chars[char][0], num)

      if sym == "<=":
        chars[char][1] = min(chars[char][1], num)


      
    res.append(chars)
  return res


def compute_total(intervals):
  res = 0
  for map in intervals:
    cur = 1
    for char in ['x', 'm', 'a', 's']:
      cur *= map[char][1] - map[char][0] + 1
    res += cur
  return res



if __name__ == "__main__":
  print(main(workflows))