import sys

lines = sys.stdin.read().splitlines()

i = 0
for i in range(0, len(lines), 2):
    num_of_values = int(lines[i])
    numbers = [int(x) for x in lines[i+1].split()]
    
    even = False
    if num_of_values % 2 == 0:
        even = True

    medium_left = numbers[len(numbers) // 2 - 1]
    medium_right = numbers[len(numbers) // 2]
    if even:
        medium = medium_left
    else:
        medium = medium_right

    count = 0
    for i in range(0, len(numbers)):
        if numbers[i] == medium:
            count += 1

    other = 1
    if even:
        medium = medium_left
        other = medium_right - medium_left + 1
        if medium_left != medium_right:
            count += 1
    else:
        medium = medium_right

    print(medium, count, other)
