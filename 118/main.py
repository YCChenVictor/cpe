import sys

data = sys.stdin.buffer.read().split()
i = 0

regionX = int(data[0])
regionY = int(data[1])

i += 2

scents = set()

while i < len(data):
    nx = int(data[i]); ny = int(data[i+1]); orient = data[i+2].decode()
    i += 3
    movements = data[i].decode()
    i += 1

    lost = False
    for movement in movements:
        if movement == 'F':
            prevX = nx
            prevY = ny

            if orient == 'N':
                ny += 1
            elif orient == 'S':
                ny -= 1
            elif orient == 'E':
                nx += 1
            elif orient == 'W':
                nx -= 1
            
            if ((nx > regionX) | (ny > regionY) | (nx < 0) | (ny < 0)):
                nx = prevX
                ny = prevY
                if (scents.__contains__((prevX, prevY, orient))):
                    continue

                lost = True
                scents.add((prevX, prevY, orient))
                break

        elif movement == 'R':
            if orient == 'N':
                orient = 'E'
            elif orient == 'S':
                orient = 'W'
            elif orient == 'E':
                orient = 'S'
            elif orient == 'W':
                orient = 'N'
        elif movement == 'L':
            if orient == 'N':
                orient = 'W'
            elif orient == 'S':
                orient = 'E'
            elif orient == 'E':
                orient = 'N'
            elif orient == 'W':
                orient = 'S'

    if lost:
        print(nx, ny, orient, "LOST")
    else:
        print(nx, ny, orient)
    
    
    
    
