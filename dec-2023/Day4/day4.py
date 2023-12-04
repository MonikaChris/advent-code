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

# Part 2 main function
def countCards(cards):
  res = 0
  counts = getMatchCounts(cards) # [[card_id_number, matches, # of copies]]

  for card_id, points, num in counts:
    i = card_id - 1
    for p in range(1, points + 1):
      counts[i+p][2] += counts[i][2]
  for card in counts:
    res += card[2]
  return res

def getMatchCounts(cards):
  # Initializes point_counts array
  match_counts = [[0, 0, 1] for _ in range(len(cards))] # [card_id_number, matches, # of copies]
  for i, card in enumerate(cards):
    winNums, playNums = getNums(card)
    matches = getMatches(winNums, playNums)
    match_counts[i][0] = i + 1
    match_counts[i][1] = matches
  
  return match_counts

def getMatches(winNums, playNums):
  winners = set(winNums)
  return sum(num in playNums for num in winNums)


# Part 1 main function
def getTotalPoints(cards):
  res = 0
  for card in cards:
    winNums, playNums = getNums(card)
    points = getPoints(winNums, playNums)
    res += points
  return res

def getPoints(winNums, playNums):
  winSet = set(winNums)
  count = 0
  for num in playNums:
    if num in winSet:
      count += 1
  points = 2 ** (count - 1) if count > 0 else 0
  return points

def getNums(card):
  # Process string to get both sets of numbers
  card = card.split(':')[1]
  card.strip()
  nums1, nums2 = card.split('|')

  nums1 = nums1.split()
  nums2 = nums2.split()

  nums1 = [int(num) for num in nums1]
  nums2 = [int(num) for num in nums2]
  
  return nums1, nums2



if __name__ == "__main__":
  # total = getPoints(lines)
  # print(total)

  total = countCards(lines)
  print(total)