right, upper = map(int, input().split())

scent = set()

while True:
    try:
        x, y, d = input().split()
        x = int(x)
        y = int(y)
        i_s = input()
        lost = False
        for i in i_s:
            if i == "L":
                if d == "N":
                    d = "W"
                elif d == "S":
                    d = "E"
                elif d == "E":
                    d = "N"
                elif d == "W":
                    d = "S"
            elif i == "R":
                if d == "N":
                    d = "E"
                elif d == "S":
                    d = "W"
                elif d == "E":
                    d = "S"
                elif d == "W":
                    d = "N"
            else:  # F
                nx, ny = x, y
                if d == "N":
                    ny += 1
                elif d == "S":
                    ny -= 1
                elif d == "W":
                    nx -= 1
                elif d == "E":
                    nx += 1
                if nx > right or ny > upper or nx < 0 or ny < 0:
                    if (x, y) in scent:
                        continue
                    else:
                        scent.add((x, y))
                        lost = True
                        break
                else:
                    x, y = nx, ny
        if lost:
            print(x, y, d, "LOST")
        else:
            print(x, y, d)
    except EOFError:
        break
