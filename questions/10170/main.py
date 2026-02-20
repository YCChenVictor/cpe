import sys

lines = sys.stdin.read().splitlines()

for line in lines:
    [initial_members, specific_day] = line.split()
    answer = int(initial_members)
    addons = int(initial_members)
    while addons < int(specific_day):
        addons += (answer + 1)
        answer += 1

    print(answer)
