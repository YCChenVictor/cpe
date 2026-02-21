import sys
import math

lines = sys.stdin.read().splitlines()

for line in lines:
    [distance, angle, unit] = line.split()

    distance = int(distance)
    angle = int(angle)    

    degree = 0
    if unit == 'deg':
        degree = angle
    else:
        degree = angle / 60

    degree = degree % 360
    degree = min(360 - degree, degree)

    radius = distance + 6440
 
    arc = 2 * math.pi * radius * degree/360
    chord = 2 * math.sin((degree/360 * 2 * math.pi) / 2) * radius

    print(f"{round(arc, 6):.6f}", f"{round(chord, 6):.6f}")
