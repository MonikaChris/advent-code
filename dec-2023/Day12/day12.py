import re

test_records = [
  [['?', '?', '?', '.', '#', '#', '#'], [1, 1, 3]], 
  [['.', '?', '?', '.', '.', '?', '?', '.', '.', '.', '?', '#', '#', '.'], [1, 1, 3]], 
  [['?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?'], [1, 3, 1, 6]], 
  [['?', '?', '?', '?', '.', '#', '.', '.', '.', '#', '.', '.', '.'], [4, 1, 1]], 
  [['?', '?', '?', '?', '.', '#', '#', '#', '#', '#', '#', '.', '.', '#', '#', '#', '#', '#', '.'], [1, 6, 5]], 
  [['?', '#', '#', '#', '?', '?', '?', '?', '?', '?', '?', '?'], [3, 2, 1]]
  ]

with open('Day12/data.txt', 'r') as file:
  lines = file.readlines()

records = []
for line in lines:
  half1, half2 = line.split()
  records.append([list(half1), [int(char) for char in half2.split(',')]])


def main(records):
  res = 0
  for record in records:
    res += get_arrangements(record)
  return res

def get_arrangements(record):
  perms = get_permutations(record)
  return get_matches(perms, record)

def get_permutations(record):
  rec = record[0]
  perms = []

  def dfs(i, bad, cur_str):
    if i >= len(rec):
      perms.append(cur_str)
      return
    if rec[i] != "?":
      dfs(i+1, bad, cur_str + rec[i])
    else:
      if bad > 0:
        dfs(i+1, bad - 1, cur_str + "#")
      dfs(i+1, bad, cur_str + ".")
  
  dfs(0, sum(record[1]), "")
  return perms

def get_matches(perms, record):
  nums = record[1]
  pattern = r'^\.*'

  # Make pattern: r'^\.*#{num}\.+#{num}\.+#{num}\.*$'
  for num in nums:
    pattern += '#{' + str(num) + '}\.+'
  pattern = pattern[:-1] + '*$'

  # Count matches
  matches = 0
  for p in perms:
    if re.match(pattern, p):
      matches += 1
  return matches



if __name__ == "__main__":
  # get_arrangements(test_records[0])
  # matches = get_matches(['###.###', '##..###', '#.#.###', '#...###', '.##.###', '.#..###', '..#.###', '....###'], [['?', '?', '?', '.', '#', '#', '#'], [1, 1, 3]])
  print(main(records))