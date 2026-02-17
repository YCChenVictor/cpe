import sys

data = sys.stdin.read().strip()

collect = {}
for i in range(0, len(data)):
    current_letter = data[i].upper()
    if not ("A" <= current_letter <= "Z"):
        continue

    count = collect.get(current_letter)

    if count is None:
        collect[current_letter] = 1
    else:
        collect[current_letter] += 1

collect2 = {}
numbers = set()
for k, v in collect.items():
    exist = collect2.get(v)
    if exist is None:
        collect2[v] = []
    collect2[v].append(k)
    numbers.add(v)
numbers = sorted(numbers)
numbers.reverse()

for i in range(0, len(numbers)):
    letters = collect2[numbers[i]]
    letters.sort()
    for k in range(0, len(letters)):
        print(f"{letters[k]} {numbers[i]}")
