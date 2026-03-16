# init: 1, 2, 3 -> top, north, west

while True:
    try:
        moves = int(input())
        if moves == 0:
            break
        top, north, west, bottom, south, east = 1, 2, 3, 6, 5, 4
        for move in range(moves):
            direction = input()
            if direction == "north":
                top, bottom, north, south = south, north, top, bottom
            if direction == "south":
                top, bottom, north, south = north, south, bottom, top
            if direction == "east":
                top, west, bottom, east = west, bottom, east, top
            if direction == "west":
                top, west, bottom, east = east, top, west, bottom
        print(top)
    except EOFError:
        break
