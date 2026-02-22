import sys

lines = sys.stdin.read().splitlines()

for i in range(0, len(lines), 2):
    input = int(lines[i])
    degrees = lines[i+1].split()
    n = len(degrees) - 1
    derivates = [(n - x) * int(degrees[x]) for x in range(0, len(degrees) - 1)]
    values = [derivates[x] * input ** (len(derivates) - x - 1) for x in range(0, len(derivates))]
    print(sum(values))

