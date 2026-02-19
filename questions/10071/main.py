import sys

lines = sys.stdin.read().splitlines()

for line in lines:
    numbers = line.split()
    velocity = int(numbers[0])
    time = int(numbers[1])
    print(2 * velocity * time)
