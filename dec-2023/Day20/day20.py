from nodes import Mod, Flipflop, Conjunction
from collections import deque

def get_node_map(filename):
  with open(f'Day20/{filename}', 'r') as file:
    lines = file.readlines()

  node_map = {}
  for line in lines:
    node, neighbors = (part.strip() for part in line.split("->"))
    neighbors = [neigh.strip() for neigh in neighbors.split(',')]
    node_map[node] = neighbors
  return node_map


def get_nodes(node_map):
  node_types = {'%': Flipflop, '&': Conjunction}
  nodes = {}
  for node, neighbors in node_map.items():
    if node[0] in node_types:
      nodes[node[1:]] = (node_types[node[0]](node[1:]))
    
    for neigh in neighbors:
      if neigh not in nodes:
        new_node = Mod(neigh)
        nodes[neigh] = new_node
  return nodes


def get_adj_lst(nodes, node_map):
  adj_lst = {}
  for node, neighbors in node_map.items():
    if node == "broadcaster":
      continue
    key = nodes[node[1:]]
    value = [nodes[neigh] for neigh in neighbors]
    adj_lst[key] = value
  return adj_lst


def bfs_pulse(adj_lst, node_map, nodes): # adj_lst: {node: [node, node]} ; node_map: {'%name' : ['name', 'name']} ; nodes: {'name' : node}
  counts = {'LOW' : 1, 'HIGH' : 0}
  q = deque()
  q.append(([nodes[node] for node in node_map['broadcaster']], 'LOW')) #([current_nodes], pulse)
  
  while q:
    node_group, pulse = q.popleft()
    
    #First process each pulse in group
    for node in node_group:
      node.pulse_in(pulse)
      # print(pulse)
      counts[pulse] += 1

    #Then propagate additional pulses
    for node in node_group:
      pulse = node.pulse_out()
      if pulse:
        q.append((adj_lst[node], pulse))
  return counts['LOW'], counts['HIGH']


def main(filename, button_presses):
  node_map = get_node_map(filename)
  # print(node_map)
  nodes = get_nodes(node_map)
  # print(nodes)
  adj_lst = get_adj_lst(nodes, node_map)
  # print(adj_lst)

  low = 0
  high = 0
  for _ in range(button_presses):
    low_count, high_count = bfs_pulse(adj_lst, node_map, nodes)
    low += low_count
    high += high_count
  return low * high



if __name__ == "__main__":
  print(main('test2.txt', 1000))
    





