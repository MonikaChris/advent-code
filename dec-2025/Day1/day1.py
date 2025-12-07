with open("Day1/data.txt", "r") as file:
  lines = file.readlines()
data = [line.strip() for line in lines]

sampleData = [
  "L68",
  "L30",
  "R48",
  "L5",
  "R60",
  "L55",
  "L1",
  "L99",
  "R14",
  "L82"
]

def safeDial(input):
  zerosCount = 0
  start = 50
  for value in input:
    num = int(value[1:]) * -1 if value[0] == "L" else int(value[1:])
    start = (start + num)%100
    if start == 0:
      zerosCount += 1
  return zerosCount


if __name__ == "__main__":
  print(safeDial(sampleData))
  print(safeDial(data))
