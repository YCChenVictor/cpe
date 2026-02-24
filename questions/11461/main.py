import sys
import math

lines = sys.stdin.read().splitlines()

def is_square(n):
    if n == 0:
         return False

    return n == math.isqrt(n) ** 2

for line in lines:
    [start, end] = line.split()
    start = int(start)
    end = int(end)

    answer = math.isqrt(end) - math.isqrt(start)
    if is_square(start):
        answer += 1

    print(answer)
