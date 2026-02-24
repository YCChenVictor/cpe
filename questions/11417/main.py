import sys
import math

lines = sys.stdin.read().splitlines()

for line in lines:
    G = 0
    for i in range(1, int(line)):
        for j in range(i+1, int(line)+1):
            G += math.gcd(i, j)

    print(G)
