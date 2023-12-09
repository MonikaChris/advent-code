with open('Day7/data.txt', 'r') as file:
  lines = file.readlines()
lines = [line.strip().split() for line in lines]
lines = [[sublist[0], int(sublist[1])] for sublist in lines]

test_cards = [['32T3K', 765], ['T55J5', 684], ['KK677', 28], ['KTJJT', 220], ['QQQJA', 483]]

cards = {
  '2' : 2,
  '3' : 3,
  '4' : 4,
  '5' : 5,
  '6' : 6,
  '7' : 7,
  '8' : 8,
  '9' : 9,
  'T': 10,
  'J' : 11,
  'Q' : 12,
  'K' : 13,
  'A' : 14
}


def main(cards):
  mergeCards(cards)
  res = 0
  for i in range(len(cards)):
    res += (i + 1) * cards[i][1]
  return res
  

def mergeCards(cards):
  if len(cards) > 1:
      mid = len(cards) // 2
      l = cards[:mid]
      r = cards[mid:]

      mergeCards(l)
      mergeCards(r)

      i = j = k = 0

      while i < len(l) and j < len(r):
          if not hand1isGreaterOrEqual(l[i][0], r[j][0]):
              cards[k] = l[i]
              i += 1
          else:
              cards[k] = r[j]
              j += 1
          k += 1

      while i < len(l):
          cards[k] = l[i]
          i += 1
          k += 1

      while j < len(r):
          cards[k] = r[j]
          j += 1
          k += 1


def hand1isGreaterOrEqual(hand1, hand2):
  counts1 = getCounts(hand1)
  counts2 = getCounts(hand2)

  hand1_counts = sorted(list(counts1.values()), reverse=True)
  hand2_counts = sorted(list(counts2.values()), reverse=True)

  # Check for winning hand
  for i in range(max(len(hand1_counts), len(hand2_counts))):
    if i >= len(hand1_counts):
      return True
    if i >= len(hand2_counts):
      return False
    if hand1_counts[i] > hand2_counts[i]:
      return True
    if hand1_counts[i] < hand2_counts[i]:
      return False
  
  # Tie breaker
  for i in range(len(hand1)):
    if cards[hand1[i]] > cards[hand2[i]]:
      return True
    if cards[hand1[i]] < cards[hand2[i]]:
      return False
  return True
  
    
def getCounts(hand):
  counts = {}
  for card in hand:
    counts[card] = 1 + counts.get(card, 0)
  return counts
  

if __name__ == "__main__":
  print(main(lines))