import sys

lines = sys.stdin.read().splitlines()

num_of_commands = 0
i = 0
while int(lines[i]) != 0:
    num_of_commands = int(lines[i])
    i += 1
    top, bottom, north, south, west, east = 1, 6, 2, 5, 3, 4
    for j in range(i, i + num_of_commands):
        command = lines[j]
        if command == 'north':
            top, bottom, north, south = south, north, top, bottom
        if command == 'south':
            top, bottom, north, south = north, south, bottom, top
        if command == 'east':
            top, west, bottom, east = west, bottom, east, top
        if command == 'west':
            top, east, west, bottom = east, bottom, top, west
    print(top)
    i += num_of_commands
    num_of_commands = int(lines[i])
