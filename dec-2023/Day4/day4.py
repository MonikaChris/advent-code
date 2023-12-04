with open('Day4/data.txt', 'r') as file:
  lines = file.readlines()
lines = [line.strip() for line in lines]

test_card = [
  "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
  "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
  "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
  "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
  "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
  "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]

def getPoints(cards):
  res = 0
  for card in cards:
    winNums, playNums = getNums(card)
    
    winSet = set()
    count = 0
    for num in winNums:
      winSet.add(num)
    for num in playNums:
      if num in winSet:
        count += 1
    points = 2 ** (count - 1) if count > 0 else 0
    res += points
  return res

def getNums(card):
  card = card.split(':')[1]
  card.strip()
  nums1, nums2 = card.split('|')

  nums1 = nums1.split()
  nums2 = nums2.split()

  nums1 = [int(num) for num in nums1]
  nums2 = [int(num) for num in nums2]
  
  return nums1, nums2



if __name__ == "__main__":
  total = getPoints(lines)
  print(total)