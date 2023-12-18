test_records = [
  ['???.###', [1, 1, 3]], 
  ['.??..??...?##.', [1, 1, 3]], 
  ['?#?#?#?#?#?#?#?', [1, 3, 1, 6]], 
  ['????.#...#...', [4, 1, 1]], 
  ['????.######..#####.', [1, 6, 5]], 
  ['?###????????', [3, 2, 1]]
  ]

with open('Day12/data.txt', 'r') as file:
  lines = file.readlines()

records = []
for line in lines:
  half1, half2 = line.split()
  records.append([half1, [int(char) for char in half2.split(',')]])

EXP_COEF = 5 # Expansion coefficient
 
def main(records):
  cache = {}
  res = 0
  for record in records:
    expanded_record = expand(record)
    res += get_counts(expanded_record, cache)
  return res


def expand(record):
  text = record[0]
  groups = record[1]

  expanded_text = text
  for _ in range(EXP_COEF - 1):
    expanded_text += "?" + text
  
  expanded_groups = groups * EXP_COEF

  return [expanded_text, expanded_groups]


def get_counts(record, cache):
  text = record[0]
  groups = record[1]

  def check(text, groups):
    if (text, tuple(groups)) in cache:
      return cache[(text, tuple(groups))]
    if not text and not groups:
      return 1
    if not groups and "#" not in text:
      return 1
    if not text or not groups:
      return 0
    
    count = 0

    if text[0] == ".":
      count += check(text[1:], groups)
    elif text[0] == "?":
      count += check("." + text[1:], groups)
      count += check("#" + text[1:], groups)
    elif text[0] == "#":
      for i in range(groups[0]):
        if i >= len(text) or text[i] == ".":
          return 0
      if groups[0] < len(text) and text[groups[0]] == "#": # dots must separate groups, so need ? or . after last #, unless end of text
        return 0
      else:
        count += check(text[1 + groups[0]:], groups[1:].copy())
    
    cache[(text, tuple(groups))] = count
    return count
  
  return check(text, groups)



if __name__ == "__main__":
  print(main(records))
  
  
  
