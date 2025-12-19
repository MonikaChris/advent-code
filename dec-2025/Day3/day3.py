with open("Day3/data.txt", "r") as file:
  lines = file.readlines()
data = [line.strip() for line in lines]

sampleData = [
  "987654321111111",
  "811111111111119",
  "234234234234278",
  "818181911112111"
]

def maxJoltage(batteries):
  total = 0
  for battery in batteries:
    firstMax = max(battery[:-1])
    i = battery.index(firstMax)
    secondMax = max(battery[i+1:])
    total += int(firstMax + secondMax)
  return total
    
if __name__ == "__main__":
  print(maxJoltage(sampleData))
  print(maxJoltage(data))
  