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
    startIndex = 0
    endIndex = len(battery) - 11
    voltage = ""

    while endIndex <= len(battery):
      maxFound = max(battery[startIndex:endIndex])
      voltage += maxFound
      startIndex += battery[startIndex:endIndex].index(maxFound) + 1
      endIndex += 1
    total += int(voltage)
    
  return total


if __name__ == "__main__":
  print(maxJoltage(sampleData))
  print(maxJoltage(data))
