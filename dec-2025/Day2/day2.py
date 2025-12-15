with open("Day2/data.txt", "r") as file:
  data = file.read().strip().split(",")

sampleData = [
  "11-22",
  "95-115",
  "998-1012",
  "1188511880-1188511890",
  "222220-222224",
  "1698522-1698528",
  "446443-446449",
  "38593856-38593862",
  "565653-565659",
  "824824821-824824827",
  "2121212118-2121212124"
]

def isRepeatedSequence(num):
  if len(num)%2== 1:
    return False
  
  mid = len(num)//2
  l, r = 0, mid

  while r < len(num):
    if num[l] != num[r]:
      return False
    l += 1
    r += 1

  return True


def findInvalidIds(idRanges):
  count = 0
  for idRange in idRanges:
    start, end = idRange.split("-")
    for num in range(int(start), int(end) + 1):
      if isRepeatedSequence(str(num)):
        count += num
  return count

if __name__ == "__main__":
  print(findInvalidIds(sampleData))
  print(findInvalidIds(data))