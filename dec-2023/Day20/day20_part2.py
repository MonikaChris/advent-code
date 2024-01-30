#Part 2 Brute Force Solution - too slow

from nodes2 import Rx, Flipflop, Conjunction
from collections import deque

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
        new_node = Rx(neigh)
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


def set_conjunction_node_memory(adj_lst, node_map, nodes):
  for node in node_map.keys():
    if node != "broadcaster":
      for neigh in adj_lst[nodes[node[1:]]]:
        if type(neigh) == Conjunction:
          neigh.add_input_node(nodes[node[1:]])


def bfs_pulse(adj_lst, node_map, nodes): # adj_lst: {node: [node, node]} ; node_map: {'%name' : ['name', 'name']} ; nodes: {'name' : node}
  counts = {'LOW' : 1, 'HIGH' : 0}
  q = deque()
  q.append(('broadcaster', [nodes[node] for node in node_map['broadcaster']], 'LOW')) #(prev_node, [current_nodes], pulse)
  
  while q:
    prev, node_group, pulse = q.popleft()
    
    #First process each pulse in group
    for node in node_group:
      node.pulse_in(prev, pulse)
      counts[pulse] += 1

    #Then propagate additional pulses
    for node in node_group:
      pulse = node.pulse_out()
      if pulse:
        q.append((node, adj_lst[node], pulse))
  return counts['LOW'], counts['HIGH']


# def main(filename, button_presses):
#   node_map = get_node_map(filename)
#   nodes = get_nodes(node_map)
#   adj_lst = get_adj_lst(nodes, node_map)
#   set_conjunction_node_memory(adj_lst, node_map, nodes)

#   low = 0
#   high = 0
#   for _ in range(button_presses):
#     low_count, high_count = bfs_pulse(adj_lst, node_map, nodes)
#     low += low_count
#     high += high_count
#   return low * high

def main(filename):
  node_map = get_node_map(filename)
  nodes = get_nodes(node_map)
  adj_lst = get_adj_lst(nodes, node_map)
  set_conjunction_node_memory(adj_lst, node_map, nodes)
  rx = nodes['rx']

  count = 0
  rx_val = 0
  while rx_val != 1:
    bfs_pulse(adj_lst, node_map, nodes)
    rx_val = rx.get_low_count()
    print(rx_val)
    count += 1

  return count



if __name__ == "__main__":
  print(main('data.txt'))
    





