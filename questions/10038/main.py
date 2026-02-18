import sys

for line in sys.stdin:
    line = line.rstrip("\n")
    numbers = line.split()
    numbers.append(numbers[len(numbers) - 1])
    seen = [False] * (len(numbers) - 2)
    for i in range(2, len(numbers)):
        abs_difference = abs(int(numbers[i]) - int(numbers[i - 1]))
        if abs_difference > len(seen) - 1:
            break
        seen[abs_difference] = True

    if all(seen):
        print("Jolly")
    else:
        print("Not jolly")
