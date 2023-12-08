from almanac import create_almanac

almanac = create_almanac('Day5/data.txt')
      
lst_of_maps = ["seed-to-soil map:", 
              "soil-to-fertilizer map:", 
              "fertilizer-to-water map:", 
              "water-to-light map:", 
              "light-to-temperature map:", 
              "temperature-to-humidity map:", 
              "humidity-to-location map:"
              ]


def reformatMaps():
  # Converts each map to sorted intervals of integers
  res = []
  for map in lst_of_maps:
    vals = almanac[map]
    for str in vals:
      new_vals = str.split()
      new_vals = [int(val) for val in new_vals]
      res.append(new_vals)
    res.sort(key=lambda x: x[1])
    almanac[map] = res
    res = []

def reformatSeeds():
  res = []
  seeds = almanac["seeds"]
  for i in range(0, len(seeds) - 1, 2):
    res.append([int(seeds[i]), int(seeds[i + 1])])
  almanac["seeds"] = res

def main():
  # Reformat almanac with int values
  reformatMaps()
  reformatSeeds()

  transformed = almanac["seeds"]
  res = float("inf")

  for map in lst_of_maps:
    transformed = transformSeeds(transformed, almanac[map])
  
  for pair in transformed:
    res = min(res, pair[0])
  return res
  
# Takes all seeds and ONE map from almanac
# For each seed group, finds map interval corresponding to first seed
# Splits up seed intervals as necessary - transforms buckets of seeds once they fit a map interval
# Returns array of new seed intervals that have all been transformed by one map
def transformSeeds(seeds, mappings):
  res = []
  cur_batch = seeds.pop() if seeds else ""
  while cur_batch:
    for i, map in enumerate(mappings):
      map_start, map_end = map[1], map[1] + map[2] - 1    
      seed_start, seed_end = cur_batch[0], cur_batch[0] + cur_batch[1] - 1
      
      #Case 1: map interval contains seed interval
      #        o----o seed
      #       o-------o map
      if seed_start >= map_start and seed_end <= map_end:
        res.append(transform(cur_batch, map))
        cur_batch = seeds.pop() if seeds else ""
        break

      #Case 2: Overlap
      #     o--------o seed
      #           o----------o map
      if seed_start < map_start and seed_end >= map_start and seed_end <= map_end:
        first_half = [seed_start, map_start - seed_start] # No +1 on interval b/c not inclusive of map start boundary
        second_half = [map_start, seed_end - map_start + 1] # +1 on interval b/c includes both boundary points
        res.append(transform(second_half, map))
        cur_batch = first_half
        break

      #Case 3: Overlap
      #        o---------o seed
      #    o---------o map
      if seed_start >= map_start and seed_start <= map_end and seed_end > map_end:
        first_half = [seed_start, map_end - seed_start + 1] # +1 on interval b/c includes both boundary points
        second_half = [map_end + 1, seed_end - map_end]
        res.append(transform(first_half, map))
        cur_batch = second_half
        break

      #Case 4: Overlap
      #  o----------o seed
      #     o----o map
      if seed_start < map_start and seed_end > map_end:
        first_third = [seed_start, map_start - seed_start] # No +1 b/c not including boundary
        second_third = [map_start, map_end - map_start + 1] #+1 b/c including both boundary points
        third_third = [map_end + 1, seed_end - map_end] #+1 eaten by: -(map_end + 1) + 1
        res.append(transform(second_third, map))
        cur_batch = first_third
        seeds.append(third_third)
        break
      
      #Case 5: No match on any interval
      if i >= len(mappings) - 1:
        res.append(cur_batch)
        cur_batch = seeds.pop() if seeds else ""
  return res

def transform(seed_range, map):
  # seed_range: [start, range]; map: [dest, src, range]
  offset = seed_range[0] - map[1]
  new_start = map[0] + offset
  return [new_start, seed_range[1]]


if __name__ == "__main__":
  print(main())

  # reformatMaps()
  # reformatSeeds()
  # print(almanac)

  # transformSeeds([[79, 14], [55, 13]], [[52, 50, 48], [50, 98, 2]])
  # transformSeeds([[57, 13], [81, 14]], [[39, 0, 15], [0, 15, 37], [37, 52, 2]])