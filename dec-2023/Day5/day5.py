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

def get_locations():
  seeds = almanac["seeds"]
  locations = []
  for seed in seeds:
    locations.append(transform(int(seed)))
  return min(locations)

def transform(seed):
  num = seed
  for map in lst_of_maps:
    ranges = almanac[map]
    for range in ranges:
      dest_start, src_start, interval = [int(num) for num in range.split()]
      src_end = src_start + interval
      if num >= src_start and num <= src_end:
        diff = num - src_start
        num = dest_start + diff
        break
  return num


if __name__ == "__main__":
  total = get_locations()
  print(total)

  # print(almanac["seed-to-soil map:"])
  # print(almanac)
 