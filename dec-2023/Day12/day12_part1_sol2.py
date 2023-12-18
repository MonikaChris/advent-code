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


def main(records):
  res = 0
  for record in records:
    res += get_counts(record)
  return res

def get_counts(record):
  text = record[0]
  groups = record[1]

  def check(text, groups):
    # print(f'text: {text} groups: {groups}')
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
    
    return count
  
  return check(text, groups)



if __name__ == "__main__":
  print(main(records))
  # print(get_counts(['???.###', [1,1,3]]))
  # print(get_counts(['.??..??...?##.', [1,1,3]]))
  # print(get_counts(['?#?#?#?#?#?#?#?', [1,3,1,6]]))
  # print(get_counts(['????.#...#...', [4,1,1]]))
  # print(get_counts(['????.######..#####.', [1,6,5]]))
  #print(get_counts(['?###????????', [3,2,1]]))
  # print(get_counts(['..', []]))
  
