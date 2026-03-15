import math

# arc = 2 * pi * r * theta/360
# chord = 2 * r * sin(theta/2)

while True:
    try:
        s, a, unit = input().split()
        s = int(s)
        a = int(a)

        if unit == "min":
            a = a / 60

        a = min(a, 360 - a)

        r = 6440 + s

        rad = 2 * math.pi * (a/360)
        
        arc = 2 * math.pi * r * (a/360)
        chord = 2 * r * math.sin(rad/2)
        print(f"{arc:.6f}", f"{chord:.6f}")
    except EOFError:
        break
