with open('Day15/data.txt', 'r') as file:
  lines = file.readlines()
lines = lines[0].split(',')

test = ['rn=1', 'cm-', 'qp=3', 'cm=2', 'qp-', 'pc=4', 'ot=9', 'ab=5', 'pc-', 'pc=6', 'ot=7']

def main(codes):
  boxes = [[] for _ in range(256)]
  for code in codes:
    if "=" in code:
      label, num = code.split('=')
    else:
      label, num = code.split('-')
    box = hash(label)
    if '=' in code:
      handle_equals(code, boxes[box])
    else:
      handle_dash(code, boxes[box])
  return tally(boxes)


def handle_equals(code, box):
  label, num = code.split('=')
  
  for i, lens in enumerate(box):
    lens_label, lens_num = lens.split()
    if label == lens_label:
      box[i] = label + " " + num
      return
  box.append(label + " " + num)
  return


def handle_dash(code, box):
  label, num = code.split('-')
  for lens in box:
    lens_label, lens_num = lens.split()
    if label == lens_label:
      box.remove(lens_label + " " + lens_num)
      return


def tally(boxes):
  res = 0
  for i, box in enumerate(boxes):
    count = 1
    if len(box) > 0:
      for lens in box:
        label, num = lens.split(' ')
        res += (1+i) * count * int(num)
        count += 1
  return res


def hash(code):
  res = 0
  for char in code:
    res = ((res + ord(char)) * 17) % 256
  return res



if __name__ == "__main__":
  print(main(lines))