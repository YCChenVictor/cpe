import sys

lines = sys.stdin.read().splitlines()

num_of_lines = int(lines[0])
map = {}
for i in range(1, num_of_lines + 1):
    [country, first_name, last_name] = lines[i].split()
    if map.get(country) == None:
        map[country] = set()
    map[country].add(" ".join([first_name, last_name]))

country_names = list(map.keys())
country_names.sort()
for country in country_names:
    print(f"{country} {len(map[country])}")
