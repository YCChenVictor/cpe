import sys

data = sys.stdin.read().splitlines()

for line in data:
    numbers = line.split()
    print(abs(int(numbers[0]) - int(numbers[1])))
