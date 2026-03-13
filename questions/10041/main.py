import sys

# Ok, then input GPT to gradually correct the answers

lines = sys.stdin.read().splitlines()

for i in range(1, len(lines)):
    current_line = lines[i]
    raw_numbers = current_line.split()
    num_of_numbers = int(raw_numbers[0])
    numbers = [int(raw_numbers[j]) for j in range(1, num_of_numbers + 1)]
    numbers.sort()

    sum = 0
    medium = numbers[num_of_numbers // 2]
    for num in numbers:
        sum += abs(medium - num)
    print(sum)
