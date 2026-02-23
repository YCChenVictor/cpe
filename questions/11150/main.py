import sys
import math

lines = sys.stdin.read().splitlines()

def change(n):
    if n == 4:
        return 2
    if n == 3:
        return 1
    if n == 2:
        return 1
    if n == 1:
        return 0

    if n % 3 == 0:
        b = 0
    else:
        b = 3 - n % 3

    add = (n + b) / 3

    return add + change(add - b)

    

for line in lines:
    init = float(line)
    print(int(init + change(init)))
