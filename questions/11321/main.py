import sys

lines = sys.stdin.read().splitlines()

i = 0
while i < len(lines):
    if lines[i] == "":
        break
    [num_of_nums, base] = lines[i].split()
    num_of_nums = int(num_of_nums)
    base = int(base)
    i += 1
    values = []
    for j in range(i, i + num_of_nums):
        values.append(int(lines[j]))
    values.sort()
    collection = {}
    for m in range(0, len(values)):
        current = values[m]
        if current < 0:
            mod = -(abs(current) % base)
        else:
            mod = current % base
        if collection.get(mod) is None:
            collection[mod] = []
        if current % 2 == 0:
            collection[mod] = collection[mod] + [current]
        else:
            collection[mod] = [current] + collection[mod]
    keys = list(collection.keys())
    keys.sort()
    print(num_of_nums, base)
    for key in keys:
        for element in collection[key]:
            print(element)
    i += num_of_nums 
    
