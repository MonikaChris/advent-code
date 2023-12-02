with open('Day2/data.txt', 'r') as file:
  lines = file.readlines()
lines = [line.strip() for line in lines]

# "Game 1: 13 red, 18 green; 5 green, 3 red, 5 blue; 5 green, 9 red, 6 blue; 3 blue, 3 green"

colors = {
  "red" : 12,
  "green" : 13,
  "blue" : 14
}

def countValidGames(games):
  res = 0
  for game in games:
    id = int(getId(game))
    rounds = getRounds(game)
    
    bad_val = False
    for round in rounds:
      rolls = getRolls(round)
      for roll in rolls:
        num, color = roll.split()
        if int(num) > colors[color]:
          bad_val = True
    if not bad_val:
      res += id
  return res

def minPower(games):
  res = 0
  for game in games:
    rounds = getRounds(game)
    max_red = 0
    max_blue = 0
    max_green = 0
    for round in rounds:
      rolls = getRolls(round)
      for roll in rolls:
        num, color = roll.split()
        if color == "red":
          max_red = max(max_red, int(num))
        if color == "blue":
          max_blue = max(max_blue, int(num))
        if color == "green":
          max_green = max(max_green, int(num))
    res += (max_red * max_blue * max_green)
  return res

def getId(game):
  game = game.split()
  return game[1].strip(':')

def getRounds(game):
  game = game.split(':')[1]
  return game.split(';')

def getRolls(round):
  return round.split(',')




if __name__ == "__main__":
  # total = countValidGames(lines)
  # print(total)

  # total = countValidGames(["Game 10: 5 green, 1 red; 5 green, 3 blue; 1 red, 7 green, 3 blue; 1 blue, 6 green; 2 green, 4 blue"])
  # print(total)

  # total = minPower(["Game 10: 5 green, 1 red; 5 green, 3 blue; 1 red, 7 green, 3 blue; 1 blue, 6 green; 2 green, 4 blue"])
  # print(total)

  total = minPower(lines)
  print(total)