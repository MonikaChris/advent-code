test = [
  ['#.##..##.',
  '..#.##.#.',
  '##......#',
  '##......#',
  '..#.##.#.',
  '..##..##.',
  '#.#.##.#.'],
  ['#...##..#',
  '#....#..#',
  '..##..###',
  '#####.##.',
  '#####.##.',
  '..##..###',
  '#....#..#']
]

test2 = [[
  '######.##',
  '##..###..',
  '.......#.',
  '#.##.#..#',
  '###.####.',
  '######..#',
  '.#..#.#.#',
  '#....###.',
  '.......##',
  '.####.##.',
  '#....#...',
  '..##....#',
  '..##....#',
  '######...',
  '.#..#..##',
  '.#..#..##',
  '######...'
]]

with open('Day13/data.txt', 'r') as file:
  lines = file.readlines()
lines = [line.strip() for line in lines]
patterns = []
pattern = []
for line in lines:
  if line:
    pattern.append(line)
  else:
    patterns.append(pattern)
    pattern = []
if pattern:
  patterns.append(pattern)



  


if __name__ == "__main__":
  print(main(patterns))
  