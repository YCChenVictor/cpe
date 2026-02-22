import sys

lines = sys.stdin.read().splitlines()

num_of_cases = int(lines[0])
for i in range(1, num_of_cases + 1):
    [a, b] = lines[i].split()
    a = int(a)
    b = int(b)
    x = (a + b) / 2
    y = (a - b) / 2
    

    if (y < 0 or x % 1 != 0 or y % 1 != 0):
        print("impossible")
    else:
        print(int(x), int(y))
