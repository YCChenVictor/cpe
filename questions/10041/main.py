import sys

data = sys.stdin.read().splitlines()

for i in range(1, len(data)):
    line = data[i]
    numbers = line.split()
    num_of_relative = int(numbers[0])
    streets = list(map(int, numbers[1:]))
    streets.sort()
    medium = streets[num_of_relative // 2]
    answer = 0
    for j in range(0, len(streets)):
        answer += abs(streets[j] - medium)
        
    print(answer)
