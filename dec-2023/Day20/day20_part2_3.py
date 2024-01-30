from nodes2 import Mod, Flipflop, Conjunction
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


def set_conjunction_node_memory(adj_lst, node_map, nodes):
  for node in node_map.keys():
    if node != "broadcaster":
      for neigh in adj_lst[nodes[node[1:]]]:
        if type(neigh) == Conjunction:
          neigh.add_input_node(nodes[node[1:]])


def main(filename, targets):
  cycle_lengths = []
  for target in targets:
    node_map = get_node_map(filename)
    nodes = get_nodes(node_map)
    adj_lst = get_adj_lst(nodes, node_map)
    set_conjunction_node_memory(adj_lst, node_map, nodes)
    cycle_lengths.append(get_cycle_length(node_map, nodes, adj_lst, target))
  print(cycle_lengths)
  return math.lcm(*cycle_lengths)


def get_cycle_length(node_map, nodes, adj_lst, target):
  count = 1
  while get_pulse(node_map, nodes, adj_lst, target) != "HIGH":
    count += 1
  return count


def get_pulse(node_map, nodes, adj_lst, target):
  q = deque()
  q.append(("broadcaster", [nodes[node] for node in node_map["broadcaster"]], "LOW"))
  
  while q:
    prev, node_group, pulse = q.popleft()
    
    #First process each pulse in group
    for node in node_group:
      node.pulse_in(prev, pulse)
      
    #Then propagate additional pulses
    for node in node_group:
      pulse = node.pulse_out()
      if node.name == target and pulse == "HIGH":
        return pulse
      if pulse:
        q.append((node, adj_lst[node], pulse))
  


if __name__ == "__main__":
  node_map = get_node_map('data.txt')
  nodes = get_nodes(node_map)
  adj_lst = get_adj_lst(nodes, node_map)
  set_conjunction_node_memory(adj_lst, node_map, nodes)
  # print(get_cycle_length(node_map, nodes, adj_lst,'mk'))
  # print(get_pulse(node_map, nodes, adj_lst,'vf'))
  print(main('data.txt', ['hf', 'pk', 'pm', 'mk']))
  
