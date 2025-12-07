with open("Day1/data.txt", "r") as file:
  lines = file.readlines()
data = [line.strip() for line in lines]

# sampleData = [
#   "L68",
#   "L30",
#   "R48",
#   "L5",
#   "R60",
#   "L55",
#   "L1",
#   "L99",
#   "R14",
#   "L82"
# ]

# sampleData = [
#   "L50",
#   "R50",
#   "L50",
#   "L50",
#   "R50",
#   "L50",
#   "R50",
#   "R50"
# ]

# sampleData = [
#   "L150",
#   "L50",
#   "L150",
#   "R50",
#   "R150",
#   "L50",
#   "R150",
#   "R50",
# ]

# sampleData = [
#   "L250",
#   "R100",
#   "L100"
# ]

sampleData = [
  "L50",
  "R110"
]

def getZerosCount(num, start):
  # Case 1: start + num stays in range of 1 to 99, so will never reach zero - return 0 zeros found
  if ((num < 0 and start + num > 0) or
      (num > 0 and start + num <= 99) or
      (num == 0)):
    return 0

  # Case 2: Moving left, and start minus num goes to or beyond 0
  # Since moving left (towards 0), subtract start from num and count one zero, since reached zero by doing this
  # Then divide the diff by 100 to count how many more times 0 will be reached
  if num < 0: # num is negative when moving left
    diff = (num * -1) - start
    zeros = 0 if start == 0 else 1 #If start is 0, that means already starting from 0 based on last rotation, so don't want to double count here
    zeros += int(diff/100)
    return zeros

  # Case 3: Moving right, and adding num to start goes beyond 99
  # Since moving right, (100 - start) is the distance to zero. Subtract this from num and count one zero.
  # Then divide the diff by 100 to count how many more times 0 will be reached
  else:
    diff = num - (100 - start)
    zeros = 1 # Don't need same correction here if start is 0, because when moving right, looking at (100 - start) as distance to travel to next 0, so correctly calculates 100 steps to next 0, and you don't double count
    zeros += int(diff/100)
    return zeros
      

def safeDial(input):
  zerosCount = 0
  start = 50
  for value in input:
    num = (int(value[1:]) * -1) if value[0] == "L" else int(value[1:])
    zerosCount += getZerosCount(num, start)
    start = (start + num)%100
  return zerosCount  
  

if __name__ == "__main__":
  print(safeDial(sampleData))
  print(safeDial(data))
