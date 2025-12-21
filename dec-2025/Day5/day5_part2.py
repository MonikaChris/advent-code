with open("Day5/data.txt", "r") as file:
  part1, part2 = file.read().strip().split("\n\n")
data = part1.splitlines()

sampleData = [
  "3-5",
  "10-14",
  "16-20",
  "12-18",
]

def mergeIntervals(ranges):
  # Convert to int tuples
  intervals = []
  for r in ranges:
    start, end = r.split("-")
    interval = (int(start), int(end))
    intervals.append(interval)

  # Sort by first value in int tuple
  intervals.sort(key=lambda t: t[0])

  # Merge
  # Compare adjacent tuples, if not overlapping (end of first 
  # is less than start of second), add second tuple to result as is and continue,
  # otherwise, take start value of first one, take larger end value,
  # append this new tuple range. This merged tuple becomes the new first
  # tuple to compare against.
  
  res = [intervals[0]]
  for i in range(1, len(intervals)):
    first = res[-1]
    second = intervals[i]
    
    # Non-overlapping
    if first[1] < second[0]:
      res.append(second)
    # Overlapping  
    else:
      newInterval = (first[0], max(first[1], second[1]))
      res[-1] = newInterval
  return res


def countFresh(ranges):
  result = 0
  intervals = mergeIntervals(ranges)
  for interval in intervals:
    start, end = interval[0], interval[1]
    result += end - start + 1
  return result


if __name__ == "__main__":
  print(countFresh(sampleData))
  print(countFresh(data))