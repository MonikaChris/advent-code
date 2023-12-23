with open('Day15/data.txt', 'r') as file:
  lines = file.readlines()
lines = lines[0].split(',')

test = ['rn=1', 'cm-', 'qp=3', 'cm=2', 'qp-', 'pc=4', 'ot=9', 'ab=5', 'pc-', 'pc=6', 'ot=7']

def main(codes):
  res = 0
  for code in codes:
    res += hash(code)
  return res


def hash(code):
  res = 0
  for char in code:
    res = ((res + ord(char)) * 17) % 256
  return res



if __name__ == "__main__":
  print(main(lines))