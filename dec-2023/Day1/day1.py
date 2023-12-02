from trie import Trie

trie = Trie()
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for digit in digits:
  trie.insert(digit)

digit_map = {
  "one" : "1",
  "two" : "2",
  "three" : "3",
  "four" : "4",
  "five" : "5",
  "six" : "6",
  "seven" : "7",
  "eight" : "8",
  "nine" : "9"
}

with open('Day1/day1Data.txt', 'r') as file:
  lines = file.readlines()
lines = [line.strip() for line in lines]

def computeCalibrationVals(codes):
  total = 0
  for code in codes:
    num = getCodeNumber(code)
    total += num
  return total

def getCodeNumber(code):
  res = ""
  nums = getNums(code)
  res += digit_map[nums[0]] if nums[0] in digit_map else nums[0]
  res += digit_map[nums[-1]] if nums[-1] in digit_map else nums[-1]
  return int(res)

def getNums(word):
  res = []
  prefix = ''
  r = 0
  for l in range(len(word)):
    r = l
    while r < len(word):
      if not isNum(word[r]):
        prefix += word[r]
        if not trie.startsWith(prefix):
          prefix = ""
          break
        if trie.search(prefix):
          res.append(prefix)
          prefix = ""
          break
      else:
        res.append(word[r])
        prefix = ""
        break
      r += 1
  return res


def isNum(c):
  return (ord('0') <= ord(c) <= ord('9'))


if __name__ == '__main__':
  total = computeCalibrationVals(lines)
  print(total)
  # test = computeCalibrationVals(['fone23', 'mvhsixpptztjh13sixthree2'])
  # print(test)
