import sys

lines = sys.stdin.read().splitlines()

num_of_groups = lines[0]
num_of_pair = 0
for i in range(1, len(lines), 2):
    num_of_pair += 1
    first_one = lines[i]
    second_one = lines[i+1]
    first_divisible = int(first_one, 2) % int("11", 2)
    second_divisible = int(second_one, 2) % int("11", 2)
    if first_divisible == 0 and second_divisible == 0:
        print(f"Pair #{num_of_pair}: All you need is love!")
    else:
        print(f"Pair #{num_of_pair}: Love is not all you need!")
