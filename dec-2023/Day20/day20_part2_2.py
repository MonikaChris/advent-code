# Failed attempt - finds all paths to rx and runs those in isolation - doesn't take into account
# that additional nodes outside the path affect it

from nodes import Mod, Flipflop, Conjunction
from collections import deque
import math

def get_node_map(filename):
  #Returns node_map: { %name : [name, name, ...]}
  with open(f'Day20/{filename}', 'r') as file:
    lines = file.readlines()

  node_map = {}
  for line in lines:
    node, neighbors = (part.strip() for part in line.split("->"))
    neighbors = [neigh.strip() for neigh in neighbors.split(',')]
    node_map[node] = neighbors
  return node_map


def get_nodes(node_map):
  #Returns nodes: { name : node } 
  node_types = {'%': Flipflop, '&': Conjunction}
  nodes = {}
  for node, neighbors in node_map.items():
    if node[0] in node_types:
      nodes[node[1:]] = (node_types[node[0]](node[1:]))
    
    #Adds childless nodes with no type
    for neigh in neighbors:
      if neigh not in nodes:
        new_node = Mod(neigh)
        nodes[neigh] = new_node
  return nodes


def get_adj_lst(nodes, node_map):
  #Returns adj_lst: { name : [node, node, ...]}
  adj_lst = {}
  for node, neighbors in node_map.items():
    if node == "broadcaster":
      continue
    key = nodes[node[1:]]
    value = [nodes[neigh] for neigh in neighbors]
    adj_lst[key] = value
  return adj_lst


# def get_paths_to_node(start_node, target_name, adj_lst):
#   res = []

#   def dfs(node, target, cur_path):
#     if node not in adj_lst:
#       return
#     if node.name == target:
#       res.append(cur_path)
#       return

#     cur_path.append(node.name)

#     for neigh in adj_lst[node]:
#       dfs(neigh, target, cur_path)

#   dfs(start_node, target_name, [])
#   return res

def get_paths_to_node(start_node, target_name, adj_lst):
  res = []
  stack = [(start_node, [])]
  visited = set()

  while stack:
    node, cur_path = stack.pop()
    if node in visited:
      continue
    if node.name == target_name:
      res.append(cur_path.copy())
      continue

    new_path = cur_path.copy()
    new_path.append(node.name)
    visited.add(node)
    
    for neigh in adj_lst[node]:
      if neigh in adj_lst:
        stack.append((neigh, new_path))

  return res


def main(filename, target):
  node_map = get_node_map('data.txt')
  nodes = get_nodes(node_map)
  adj_lst = get_adj_lst(nodes, node_map)

  paths = []
  for node in node_map["broadcaster"]:
    paths.extend(get_paths_to_node(nodes[node], target, adj_lst))
  
  res = []
  print(f'paths:{paths}')
  for path in paths:
    res.append(get_cycle_length(path, nodes))

  return get_lcm(res)


def get_cycle_length(path, nodes):
  # For rx to have 1 low pulse, all input nodes must send high pulse
  # Returns cycle length for path to end in high pulse

  count = 1
  while cycle(path, nodes) != "HIGH":
    count += 1
  return count


def cycle(path, nodes):
  pulse = "LOW"
  prev = "broadcaster"
  for name in path:
    node = nodes[name]
    node.pulse_in(prev, pulse)
    prev = node
    pulse = node.pulse_out()
    print(f'name: {name}')
    print(f'pulse: {pulse}')
    if not pulse: return
  return pulse


def get_lcm(nums):
  print(f'nums: {nums}')
  cur = nums.pop()
  for num in nums:
    cur = lcm(cur, nums.pop())
  return cur

def lcm(a, b):
  return abs(a*b) // math.gcd(a, b)


if __name__ == "__main__":
  node_map = get_node_map('data.txt')
  nodes = get_nodes(node_map)
  adj_lst = get_adj_lst(nodes, node_map)
  # print(get_paths_to_node(nodes["sh"], "vf", adj_lst))
  # print(main('data.txt', 'vf'))
  print(get_cycle_length(['ps', 'gp', 'pm'], nodes))
