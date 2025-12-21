with open("Day5/data.txt", "r") as file:
  part1, part2 = file.read().strip().split("\n\n")
ranges = part1.splitlines()
numbers = part2.splitlines()

sampleRanges = [
  "3-5",
  "10-14",
  "16-20",
  "12-18",
]

sampleNumbers = [
  "1",
  "5",
  "8",
  "11",
  "17",
  "32",
]

def countFresh(intervals, ids):
  count = 0
  for i in ids:
    for interval in intervals:
      start, end = interval.split("-")
      if int(i) >= int(start) and int(i) <= int(end):
        count += 1
        break
  return count
  

if __name__ == "__main__":
  print(countFresh(sampleRanges, sampleNumbers))
  print(countFresh(ranges, numbers))