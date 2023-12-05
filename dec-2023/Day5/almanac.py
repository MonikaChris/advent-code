def create_almanac(file_path):
  almanac = {}
  with open(file_path, 'r') as file:
    lines = [line.strip() for line in file]
    cur_vals = []
    cur_key = ""
    for line in lines:
      if ":" in line and line.split(':')[1]:
        # Handles same line values format
        key, values = line.split(':')
        almanac[key] = values.split()
      elif ":" in line:
        # Handles new line values format
        if cur_key:
          almanac[cur_key] = cur_vals
          cur_key = line
          cur_vals = []
        else:
          cur_key = line
      else:
          if line:
            cur_vals.append(line)
    if cur_key:
      almanac[cur_key] = cur_vals
  return almanac
